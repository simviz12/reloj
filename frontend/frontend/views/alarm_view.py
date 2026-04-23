"""
Vista de Alarma - Permite configurar y activar/desactivar la alarma.
"""

from config.casio_theme import CasioTheme


class AlarmView:
    """
    Vista de configuración de alarma que muestra la hora configurada
    y permite ajustarla con los botones del reloj.
    """

    def __init__(self, lcd_display, alarm_service):
        """
        Inicializa la vista de alarma.

        Args:
            lcd_display: Componente LCDDisplay para renderizado.
            alarm_service: Servicio de alarma (backend).
        """
        self._lcd = lcd_display
        self._service = alarm_service
        self._blink = True
        self._editing_hours = True

    def render(self):
        """Renderiza la vista de configuración de alarma."""
        self._lcd.clear("lcd_content")
        data = self._service.get_display_dict()

        lx = CasioTheme.LCD_X + CasioTheme.LCD_PADDING
        ly = CasioTheme.LCD_Y + CasioTheme.LCD_PADDING

        # --- Título ---
        self._lcd.draw_text(
            lx + 5, ly + 8,
            "ALM",
            font=CasioTheme.FONT_LCD_LABEL,
            tag="lcd_content"
        )

        # --- Estado de la alarma ---
        state_text = "ON" if data["enabled"] else "OFF"
        state_color = CasioTheme.SEGMENT_ON if data["enabled"] else CasioTheme.SEGMENT_OFF
        self._lcd.draw_text(
            lx + CasioTheme.LCD_WIDTH - 55, ly + 8,
            state_text,
            font=CasioTheme.FONT_LCD_LABEL,
            color=state_color,
            tag="lcd_content"
        )

        # --- Línea separadora ---
        sep_y = ly + 25
        self._lcd._canvas.create_line(
            lx + 5, sep_y,
            lx + CasioTheme.LCD_WIDTH - 30, sep_y,
            fill=CasioTheme.SEGMENT_OFF, width=1, tags="lcd_content"
        )

        # --- Hora de la alarma (dígitos grandes) ---
        time_y = ly + 45
        hours_x = lx + 30

        # Horas
        self._lcd.draw_number(
            hours_x, time_y,
            data["hour"], digits=2, size="large",
            tag="lcd_content"
        )

        # Dos puntos
        colon_x = hours_x + 2 * (CasioTheme.SEGMENT_WIDTH_LARGE + 8) + 5
        self._lcd.draw_colon(
            colon_x, time_y,
            size="large", on=True,
            tag="lcd_content"
        )

        # Minutos
        minutes_x = colon_x + 14
        self._lcd.draw_number(
            minutes_x, time_y,
            data["minute"], digits=2, size="large",
            tag="lcd_content"
        )

        # --- Indicador de edición ---
        if self._blink:
            if self._editing_hours:
                underline_x = hours_x
                underline_w = 2 * (CasioTheme.SEGMENT_WIDTH_LARGE + 8) - 8
            else:
                underline_x = minutes_x
                underline_w = 2 * (CasioTheme.SEGMENT_WIDTH_LARGE + 8) - 8

            underline_y = time_y + CasioTheme.SEGMENT_HEIGHT_LARGE + 5
            self._lcd._canvas.create_line(
                underline_x, underline_y,
                underline_x + underline_w, underline_y,
                fill=CasioTheme.SEGMENT_ON, width=2, tags="lcd_content"
            )

        self._blink = not self._blink

        # --- Icono de campana si está activa ---
        if data["enabled"]:
            bell_x = lx + CasioTheme.LCD_WIDTH // 2 - 10
            bell_y = ly + 15
            self._lcd.draw_text(
                bell_x, bell_y,
                "🔔",
                font=("Arial", 10),
                tag="lcd_content"
            )

        # --- Indicador de modo ---
        mode_y = ly + CasioTheme.LCD_HEIGHT - 30
        self._lcd.draw_text(
            lx + CasioTheme.LCD_WIDTH // 2 - 10, mode_y,
            CasioTheme.MODE_ALARM,
            font=CasioTheme.FONT_MODE,
            anchor="center",
            tag="lcd_content"
        )

    def on_start_stop(self):
        """Botón ST/SP: Incrementa el valor seleccionado."""
        if self._editing_hours:
            self._service.increment_hour()
        else:
            self._service.increment_minute()

    def on_reset(self):
        """Botón RESET: Alterna entre editar horas y minutos."""
        self._editing_hours = not self._editing_hours

    def on_adjust(self):
        """Botón ADJUST: Activa/desactiva la alarma."""
        self._service.toggle_alarm()

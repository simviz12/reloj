"""
Vista de Temporizador - Muestra cuenta regresiva configurable.
Funcionalidad adicional: Temporizador con alerta al finalizar.
"""

from config.casio_theme import CasioTheme


class TimerView:
    """
    Vista del temporizador (cuenta regresiva) que permite configurar
    minutos y segundos, iniciar la cuenta atrás y alertar al finalizar.
    Esta es la funcionalidad adicional del taller.
    """

    def __init__(self, lcd_display, timer_service):
        """
        Inicializa la vista del temporizador.

        Args:
            lcd_display: Componente LCDDisplay para renderizado.
            timer_service: Servicio de temporizador (backend).
        """
        self._lcd = lcd_display
        self._service = timer_service
        self._blink = True
        self._editing_minutes = True
        self._flash = False

    def render(self):
        """Renderiza la vista del temporizador."""
        self._lcd.clear("lcd_content")
        data = self._service.get_display_dict()

        lx = CasioTheme.LCD_X + CasioTheme.LCD_PADDING
        ly = CasioTheme.LCD_Y + CasioTheme.LCD_PADDING

        # --- Título ---
        self._lcd.draw_text(
            lx + 5, ly + 8,
            "TMR",
            font=CasioTheme.FONT_LCD_LABEL,
            tag="lcd_content"
        )

        # --- Estado ---
        if data["finished"]:
            state_text = "END!"
            self._flash = not self._flash
        elif data["running"]:
            state_text = "RUN"
            self._flash = False
        else:
            state_text = "SET"
            self._flash = False

        self._lcd.draw_text(
            lx + CasioTheme.LCD_WIDTH - 55, ly + 8,
            state_text,
            font=CasioTheme.FONT_LCD_LABEL,
            tag="lcd_content"
        )

        # --- Línea separadora ---
        sep_y = ly + 25
        self._lcd._canvas.create_line(
            lx + 5, sep_y,
            lx + CasioTheme.LCD_WIDTH - 30, sep_y,
            fill=CasioTheme.SEGMENT_OFF, width=1, tags="lcd_content"
        )

        # --- Tiempo del temporizador (dígitos grandes) ---
        time_y = ly + 45

        # Si terminó, efecto de parpadeo
        if data["finished"] and self._flash:
            # No dibujar los números (efecto parpadeo)
            pass
        else:
            min_x = lx + 30

            # Minutos
            self._lcd.draw_number(
                min_x, time_y,
                data["minutes"], digits=2, size="large",
                tag="lcd_content"
            )

            # Dos puntos
            colon_x = min_x + 2 * (CasioTheme.SEGMENT_WIDTH_LARGE + 8) + 5
            self._lcd.draw_colon(
                colon_x, time_y,
                size="large", on=True,
                tag="lcd_content"
            )

            # Segundos
            sec_x = colon_x + 14
            self._lcd.draw_number(
                sec_x, time_y,
                data["seconds"], digits=2, size="large",
                tag="lcd_content"
            )

        # --- Indicador de edición (cuando no está corriendo) ---
        if not data["running"] and not data["finished"]:
            if self._blink:
                if self._editing_minutes:
                    ux = lx + 30
                else:
                    colon_x = lx + 30 + 2 * (CasioTheme.SEGMENT_WIDTH_LARGE + 8) + 5
                    ux = colon_x + 14
                uw = 2 * (CasioTheme.SEGMENT_WIDTH_LARGE + 8) - 8
                uy = time_y + CasioTheme.SEGMENT_HEIGHT_LARGE + 5
                self._lcd._canvas.create_line(
                    ux, uy, ux + uw, uy,
                    fill=CasioTheme.SEGMENT_ON, width=2, tags="lcd_content"
                )
            self._blink = not self._blink

        # --- Barra de progreso ---
        if data["total_seconds"] > 0 and not data["finished"]:
            progress_y = ly + CasioTheme.LCD_HEIGHT - 55
            bar_width = CasioTheme.LCD_WIDTH - 50
            remaining_ratio = (data["minutes"] * 60 + data["seconds"]) / data["total_seconds"]
            filled_width = int(bar_width * remaining_ratio)

            # Fondo de la barra
            self._lcd._canvas.create_rectangle(
                lx + 10, progress_y,
                lx + 10 + bar_width, progress_y + 6,
                fill=CasioTheme.SEGMENT_OFF, outline="", tags="lcd_content"
            )

            # Barra de progreso
            if filled_width > 0:
                self._lcd._canvas.create_rectangle(
                    lx + 10, progress_y,
                    lx + 10 + filled_width, progress_y + 6,
                    fill=CasioTheme.SEGMENT_ON, outline="", tags="lcd_content"
                )

        # --- Indicador de modo ---
        mode_y = ly + CasioTheme.LCD_HEIGHT - 30
        self._lcd.draw_text(
            lx + CasioTheme.LCD_WIDTH // 2 - 10, mode_y,
            CasioTheme.MODE_TIMER,
            font=CasioTheme.FONT_MODE,
            anchor="center",
            tag="lcd_content"
        )

    def on_start_stop(self):
        """Botón ST/SP: Inicia/pausa el temporizador o incrementa valor."""
        data = self._service.get_display_dict()
        if data["finished"]:
            self._service.acknowledge()
            self._service.reset()
        elif data["running"]:
            self._service.toggle()
        elif data["total_seconds"] > 0:
            self._service.toggle()
        else:
            # Incrementar el valor seleccionado cuando está en modo SET
            if self._editing_minutes:
                self._service.increment_minutes()
            else:
                self._service.increment_seconds()

    def on_reset(self):
        """Botón RESET: Reinicia o alterna campo de edición."""
        data = self._service.get_display_dict()
        if data["running"]:
            self._service.toggle()
            self._service.reset()
        elif data["finished"]:
            self._service.acknowledge()
            self._service.reset()
        else:
            self._editing_minutes = not self._editing_minutes

    def on_adjust(self):
        """Botón ADJUST: Incrementa el valor seleccionado."""
        data = self._service.get_display_dict()
        if not data["running"]:
            if self._editing_minutes:
                self._service.increment_minutes()
            else:
                self._service.increment_seconds()

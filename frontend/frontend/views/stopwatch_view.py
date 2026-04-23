"""
Vista de Cronómetro - Muestra el cronómetro con control de inicio/pausa/reinicio.
"""

from config.casio_theme import CasioTheme


class StopwatchView:
    """
    Vista del cronómetro que muestra minutos, segundos y centésimas
    con controles de inicio, pausa y reinicio.
    """

    def __init__(self, lcd_display, stopwatch_service):
        """
        Inicializa la vista del cronómetro.

        Args:
            lcd_display: Componente LCDDisplay para renderizado.
            stopwatch_service: Servicio de cronómetro (backend).
        """
        self._lcd = lcd_display
        self._service = stopwatch_service

    def render(self):
        """Renderiza la vista del cronómetro."""
        self._lcd.clear("lcd_content")
        data = self._service.get_display_dict()

        lx = CasioTheme.LCD_X + CasioTheme.LCD_PADDING
        ly = CasioTheme.LCD_Y + CasioTheme.LCD_PADDING

        # --- Título ---
        self._lcd.draw_text(
            lx + 5, ly + 8,
            "STP",
            font=CasioTheme.FONT_LCD_LABEL,
            tag="lcd_content"
        )

        # --- Estado ---
        if data["running"]:
            state_text = "RUN"
        else:
            state_text = "STOP"
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

        # --- Tiempo del cronómetro (dígitos grandes): MM:SS ---
        time_y = ly + 40
        min_x = lx + 12

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

        # --- Centésimas (dígitos pequeños) ---
        cs_x = sec_x + 2 * (CasioTheme.SEGMENT_WIDTH_LARGE + 8) + 8
        cs_y = time_y + CasioTheme.SEGMENT_HEIGHT_LARGE - CasioTheme.SEGMENT_HEIGHT_SMALL

        # Punto separador
        self._lcd.draw_dot(
            cs_x - 6, cs_y + CasioTheme.SEGMENT_HEIGHT_SMALL - 4,
            size=4, tag="lcd_content"
        )

        self._lcd.draw_number(
            cs_x, cs_y,
            data["centiseconds"], digits=2, size="small",
            tag="lcd_content"
        )

        # --- Contador de vueltas ---
        if data["lap_count"] > 0:
            self._lcd.draw_text(
                lx + CasioTheme.LCD_WIDTH // 2 - 10, ly + CasioTheme.LCD_HEIGHT - 50,
                f"LAP: {data['lap_count']}",
                font=CasioTheme.FONT_LCD_SMALL,
                tag="lcd_content"
            )

        # --- Indicador de modo ---
        mode_y = ly + CasioTheme.LCD_HEIGHT - 30
        self._lcd.draw_text(
            lx + CasioTheme.LCD_WIDTH // 2 - 10, mode_y,
            CasioTheme.MODE_STOPWATCH,
            font=CasioTheme.FONT_MODE,
            anchor="center",
            tag="lcd_content"
        )

    def on_start_stop(self):
        """Botón ST/SP: Inicia o pausa el cronómetro."""
        self._service.toggle()

    def on_reset(self):
        """Botón RESET: Reinicia el cronómetro o registra vuelta."""
        if self._service.stopwatch.running:
            self._service.lap()
        else:
            self._service.reset()

    def on_adjust(self):
        """Botón ADJUST: Sin acción en modo cronómetro."""
        pass

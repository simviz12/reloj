"""
Vista del Reloj Analógico - Renderiza las manecillas y la esfera.
"""

from config.casio_theme import CasioTheme


class ClockView:
    """
    Vista que conecta el servicio de tiempo con el componente AnalogDisplay.
    """

    def __init__(self, analog_display, clock_service):
        self._display = analog_display
        self._service = clock_service

    def render(self):
        """Obtiene la hora actual y actualiza las manecillas."""
        data = self._service.get_current_time()

        # Actualizar ventana de fecha
        self._display.draw_date_window(data["day"])

        # Actualizar sub-dial con el día de la semana
        # (Nota: En un diseño real, esto movería una manecilla)
        cx = CasioTheme.WINDOW_WIDTH // 2
        cy = CasioTheme.WINDOW_HEIGHT // 2
        r = CasioTheme.DIAL_SIZE // 2
        self._display.draw_subdial(cx - r // 2, cy, 35, data.get("day_of_week", "MI"))

        # Actualizar manecillas
        self._display.draw_hands(
            data["hours"],
            data["minutes"],
            data["seconds"]
        )

    def on_start_stop(self):
        """En modo analógico, puede usarse para iluminar o funciones especiales."""
        pass

    def on_reset(self):
        """Sin función por defecto en vista horaria."""
        pass

    def on_adjust(self):
        """Sin función por defecto en vista horaria."""
        pass

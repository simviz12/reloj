"""
Servicio del Reloj - Orquesta la lógica principal del reloj.
"""

from ..models.clock import Clock


class ClockService:
    """
    Servicio que gestiona las operaciones del reloj principal.
    Actúa como intermediario entre el modelo y la interfaz.
    """

    def __init__(self):
        self._clock = Clock()

    @property
    def clock(self):
        """Retorna la instancia del modelo Clock."""
        return self._clock

    def get_current_time(self):
        """Obtiene la hora actual formateada para la pantalla."""
        return self._clock.get_time_dict()

    def toggle_format(self):
        """Alterna el formato de hora entre 12h y 24h."""
        self._clock.toggle_format()
        return self._clock.format_24h

    def get_formatted_time(self):
        """Retorna la hora como string formateado HH:MM:SS."""
        h = self._clock.hours
        m = self._clock.minutes
        s = self._clock.seconds
        return f"{h:02d}:{m:02d}:{s:02d}"

    def get_formatted_date(self):
        """Retorna la fecha como string formateado."""
        dow = self._clock.day_of_week
        m = self._clock.month
        d = self._clock.day
        return f"{dow} {m:02d}-{d:02d}"

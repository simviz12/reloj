"""
Servicio de Cronómetro - Gestiona las operaciones del cronómetro.
"""

from ..models.stopwatch import Stopwatch


class StopwatchService:
    """
    Servicio que administra el cronómetro del reloj.
    Controla inicio, pausa, reinicio y registro de vueltas.
    """

    def __init__(self):
        self._stopwatch = Stopwatch()

    @property
    def stopwatch(self):
        """Retorna la instancia del modelo Stopwatch."""
        return self._stopwatch

    def toggle(self):
        """Alterna entre iniciar y pausar el cronómetro."""
        self._stopwatch.toggle()
        return self._stopwatch.running

    def reset(self):
        """Reinicia el cronómetro a cero."""
        self._stopwatch.reset()

    def lap(self):
        """Registra un tiempo de vuelta."""
        self._stopwatch.lap()
        return self._stopwatch.laps

    def get_display_dict(self):
        """Retorna información del cronómetro para la pantalla."""
        return self._stopwatch.get_display_dict()

    def get_formatted_time(self):
        """Retorna el tiempo del cronómetro formateado MM:SS.cc."""
        d = self._stopwatch.get_display_dict()
        return f"{d['minutes']:02d}:{d['seconds']:02d}.{d['centiseconds']:02d}"

"""
Modelo de Cronómetro - Gestiona la funcionalidad de cronómetro.
"""

import time


class Stopwatch:
    """
    Modelo del cronómetro con funciones de inicio, pausa, reinicio y vueltas.
    Mide el tiempo transcurrido con precisión de centésimas de segundo.
    """

    def __init__(self):
        self._start_time = 0
        self._elapsed = 0
        self._running = False
        self._laps = []

    @property
    def running(self):
        """Retorna True si el cronómetro está en marcha."""
        return self._running

    @property
    def elapsed(self):
        """Retorna el tiempo transcurrido en segundos."""
        if self._running:
            return self._elapsed + (time.time() - self._start_time)
        return self._elapsed

    @property
    def laps(self):
        """Retorna la lista de tiempos de vuelta."""
        return self._laps.copy()

    @property
    def hours(self):
        """Retorna las horas transcurridas."""
        return int(self.elapsed) // 3600

    @property
    def minutes(self):
        """Retorna los minutos transcurridos (dentro de la hora)."""
        return (int(self.elapsed) % 3600) // 60

    @property
    def seconds(self):
        """Retorna los segundos transcurridos (dentro del minuto)."""
        return int(self.elapsed) % 60

    @property
    def centiseconds(self):
        """Retorna las centésimas de segundo."""
        return int((self.elapsed % 1) * 100)

    def start(self):
        """Inicia o reanuda el cronómetro."""
        if not self._running:
            self._start_time = time.time()
            self._running = True

    def stop(self):
        """Pausa el cronómetro."""
        if self._running:
            self._elapsed += time.time() - self._start_time
            self._running = False

    def reset(self):
        """Reinicia el cronómetro a cero."""
        self._start_time = 0
        self._elapsed = 0
        self._running = False
        self._laps.clear()

    def lap(self):
        """Registra un tiempo de vuelta."""
        if self._running:
            self._laps.append(self.elapsed)

    def toggle(self):
        """Alterna entre inicio y pausa."""
        if self._running:
            self.stop()
        else:
            self.start()

    def get_display_dict(self):
        """Retorna diccionario con el tiempo formateado para la pantalla."""
        return {
            "minutes": self.minutes,
            "seconds": self.seconds,
            "centiseconds": self.centiseconds,
            "running": self._running,
            "lap_count": len(self._laps)
        }

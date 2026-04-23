"""
Modelo de Temporizador - Gestiona cuenta regresiva.
"""

import time


class Timer:
    """
    Modelo del temporizador con cuenta regresiva.
    Permite configurar minutos y segundos para la cuenta atrás.
    """

    def __init__(self):
        self._total_seconds = 0
        self._remaining = 0
        self._start_time = 0
        self._running = False
        self._finished = False

    @property
    def running(self):
        """Retorna True si el temporizador está en cuenta regresiva."""
        return self._running

    @property
    def finished(self):
        """Retorna True si el temporizador ha llegado a cero."""
        return self._finished

    @property
    def remaining(self):
        """Retorna los segundos restantes."""
        if self._running:
            elapsed = time.time() - self._start_time
            rem = self._remaining - elapsed
            if rem <= 0:
                self._running = False
                self._finished = True
                self._remaining = 0
                return 0
            return rem
        return self._remaining

    @property
    def minutes(self):
        """Retorna los minutos restantes."""
        return int(self.remaining) // 60

    @property
    def seconds(self):
        """Retorna los segundos restantes (dentro del minuto)."""
        return int(self.remaining) % 60

    @property
    def total_seconds(self):
        """Retorna el total de segundos configurados."""
        return self._total_seconds

    def set_time(self, minutes, seconds=0):
        """Configura el tiempo del temporizador."""
        self._total_seconds = minutes * 60 + seconds
        self._remaining = self._total_seconds
        self._finished = False

    def increment_minutes(self):
        """Incrementa los minutos configurados en 1."""
        total_min = self._total_seconds // 60
        total_sec = self._total_seconds % 60
        total_min = (total_min + 1) % 100
        self._total_seconds = total_min * 60 + total_sec
        self._remaining = self._total_seconds
        self._finished = False

    def increment_seconds(self):
        """Incrementa los segundos configurados en 1."""
        total_min = self._total_seconds // 60
        total_sec = self._total_seconds % 60
        total_sec = (total_sec + 1) % 60
        self._total_seconds = total_min * 60 + total_sec
        self._remaining = self._total_seconds
        self._finished = False

    def start(self):
        """Inicia la cuenta regresiva."""
        if not self._running and self._remaining > 0:
            self._start_time = time.time()
            self._running = True
            self._finished = False

    def stop(self):
        """Pausa la cuenta regresiva."""
        if self._running:
            self._remaining = self.remaining
            self._running = False

    def reset(self):
        """Reinicia el temporizador al tiempo configurado."""
        self._remaining = self._total_seconds
        self._running = False
        self._finished = False

    def toggle(self):
        """Alterna entre inicio y pausa."""
        if self._running:
            self.stop()
        else:
            self.start()

    def acknowledge_finish(self):
        """Reconoce que el temporizador ha terminado."""
        self._finished = False

    def get_display_dict(self):
        """Retorna diccionario con el tiempo formateado para la pantalla."""
        return {
            "minutes": self.minutes,
            "seconds": self.seconds,
            "running": self._running,
            "finished": self._finished,
            "total_seconds": self._total_seconds
        }

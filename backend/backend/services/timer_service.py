"""
Servicio de Temporizador - Gestiona la cuenta regresiva.
"""

from models.timer import Timer


class TimerService:
    """
    Servicio que administra el temporizador del reloj.
    Controla la configuración y ejecución de la cuenta regresiva.
    """

    def __init__(self):
        self._timer = Timer()

    @property
    def timer(self):
        """Retorna la instancia del modelo Timer."""
        return self._timer

    def toggle(self):
        """Alterna entre iniciar y pausar el temporizador."""
        self._timer.toggle()
        return self._timer.running

    def reset(self):
        """Reinicia el temporizador al tiempo configurado."""
        self._timer.reset()

    def increment_minutes(self):
        """Incrementa los minutos del temporizador."""
        self._timer.increment_minutes()

    def increment_seconds(self):
        """Incrementa los segundos del temporizador."""
        self._timer.increment_seconds()

    def is_finished(self):
        """Verifica si el temporizador ha llegado a cero."""
        return self._timer.finished

    def acknowledge(self):
        """Reconoce la finalización del temporizador."""
        self._timer.acknowledge_finish()

    def get_display_dict(self):
        """Retorna información del temporizador para la pantalla."""
        return self._timer.get_display_dict()

    def get_formatted_time(self):
        """Retorna el tiempo del temporizador formateado MM:SS."""
        d = self._timer.get_display_dict()
        return f"{d['minutes']:02d}:{d['seconds']:02d}"

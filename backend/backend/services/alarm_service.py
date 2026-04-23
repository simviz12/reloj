"""
Servicio de Alarma - Gestiona las operaciones de alarma.
"""

from models.alarm import Alarm


class AlarmService:
    """
    Servicio que administra la alarma del reloj.
    Permite configurar, activar y verificar la alarma.
    """

    def __init__(self):
        self._alarm = Alarm(hour=7, minute=0, enabled=False)

    @property
    def alarm(self):
        """Retorna la instancia del modelo Alarm."""
        return self._alarm

    def increment_hour(self):
        """Incrementa la hora de la alarma."""
        self._alarm.increment_hour()

    def increment_minute(self):
        """Incrementa el minuto de la alarma."""
        self._alarm.increment_minute()

    def toggle_alarm(self):
        """Activa o desactiva la alarma."""
        self._alarm.toggle()
        return self._alarm.enabled

    def check_alarm(self):
        """Verifica si la alarma debe sonar ahora."""
        return self._alarm.check()

    def stop_ringing(self):
        """Detiene el sonido de la alarma."""
        self._alarm.stop_ringing()

    def get_display_dict(self):
        """Retorna información de la alarma para la pantalla."""
        return {
            "hour": self._alarm.hour,
            "minute": self._alarm.minute,
            "enabled": self._alarm.enabled,
            "ringing": self._alarm.ringing,
            "time_str": self._alarm.get_time_str()
        }

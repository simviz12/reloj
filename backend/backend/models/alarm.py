"""
Modelo de Alarma - Gestiona alarmas configurables.
"""

from datetime import datetime


class Alarm:
    """
    Modelo de alarma con hora, minuto y estado activo/inactivo.
    Soporta múltiples alarmas independientes.
    """

    def __init__(self, hour=0, minute=0, enabled=False):
        self._hour = hour
        self._minute = minute
        self._enabled = enabled
        self._ringing = False

    @property
    def hour(self):
        """Retorna la hora de la alarma."""
        return self._hour

    @hour.setter
    def hour(self, value):
        """Establece la hora de la alarma (0-23)."""
        self._hour = value % 24

    @property
    def minute(self):
        """Retorna el minuto de la alarma."""
        return self._minute

    @minute.setter
    def minute(self, value):
        """Establece el minuto de la alarma (0-59)."""
        self._minute = value % 60

    @property
    def enabled(self):
        """Retorna si la alarma está activa."""
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """Activa o desactiva la alarma."""
        self._enabled = value

    @property
    def ringing(self):
        """Retorna si la alarma está sonando."""
        return self._ringing

    def increment_hour(self):
        """Incrementa la hora de la alarma en 1."""
        self._hour = (self._hour + 1) % 24

    def increment_minute(self):
        """Incrementa el minuto de la alarma en 1."""
        self._minute = (self._minute + 1) % 60

    def toggle(self):
        """Alterna el estado de la alarma (activa/inactiva)."""
        self._enabled = not self._enabled

    def check(self):
        """Verifica si la alarma debe sonar en este momento."""
        if not self._enabled:
            self._ringing = False
            return False
        now = datetime.now()
        if now.hour == self._hour and now.minute == self._minute and now.second == 0:
            self._ringing = True
            return True
        if now.second != 0:
            self._ringing = False
        return False

    def stop_ringing(self):
        """Detiene el sonido de la alarma."""
        self._ringing = False

    def get_time_str(self):
        """Retorna la hora de la alarma formateada como HH:MM."""
        return f"{self._hour:02d}:{self._minute:02d}"

    def __repr__(self):
        state = "ON" if self._enabled else "OFF"
        return f"Alarm({self._hour:02d}:{self._minute:02d} [{state}])"

"""
Modelo del Reloj - Gestiona la hora actual y el formato de visualización.
"""

from datetime import datetime


class Clock:
    """
    Modelo principal del reloj digital.
    Proporciona acceso a la hora actual con soporte para formato 12/24 horas.
    """

    DAYS_ES = ["LU", "MA", "MI", "JU", "VI", "SA", "DO"]
    MONTHS_ES = [
        "ENE", "FEB", "MAR", "ABR", "MAY", "JUN",
        "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"
    ]

    def __init__(self):
        self._format_24h = False

    @property
    def now(self):
        """Retorna la hora actual del sistema."""
        return datetime.now()

    @property
    def hours(self):
        """Retorna la hora actual según el formato configurado."""
        h = self.now.hour
        if not self._format_24h:
            h = h % 12
            if h == 0:
                h = 12
        return h

    @property
    def minutes(self):
        """Retorna los minutos actuales."""
        return self.now.minute

    @property
    def seconds(self):
        """Retorna los segundos actuales."""
        return self.now.second

    @property
    def period(self):
        """Retorna AM o PM según la hora actual."""
        return "PM" if self.now.hour >= 12 else "AM"

    @property
    def day_of_week(self):
        """Retorna el día de la semana abreviado en español."""
        return self.DAYS_ES[self.now.weekday()]

    @property
    def day(self):
        """Retorna el día del mes."""
        return self.now.day

    @property
    def month(self):
        """Retorna el número del mes."""
        return self.now.month

    @property
    def month_name(self):
        """Retorna el nombre del mes abreviado en español."""
        return self.MONTHS_ES[self.now.month - 1]

    @property
    def year(self):
        """Retorna el año actual."""
        return self.now.year

    @property
    def format_24h(self):
        """Retorna True si el formato es 24 horas."""
        return self._format_24h

    def toggle_format(self):
        """Alterna entre formato 12h y 24h."""
        self._format_24h = not self._format_24h

    def get_time_dict(self):
        """Retorna un diccionario con toda la información de tiempo."""
        return {
            "hours": self.hours,
            "minutes": self.minutes,
            "seconds": self.seconds,
            "period": self.period if not self._format_24h else "",
            "day_of_week": self.day_of_week,
            "day": self.day,
            "month": self.month,
            "month_name": self.month_name,
            "year": self.year,
            "format_24h": self._format_24h
        }

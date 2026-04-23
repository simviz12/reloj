"""
Utilidades de Formato de Tiempo - Funciones auxiliares para formatear tiempo.
"""


class TimeFormatter:
    """
    Clase utilitaria con métodos estáticos para formatear valores de tiempo
    en diferentes representaciones de texto.
    """

    @staticmethod
    def format_hms(hours, minutes, seconds):
        """Formatea horas, minutos y segundos como HH:MM:SS."""
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    @staticmethod
    def format_ms(minutes, seconds):
        """Formatea minutos y segundos como MM:SS."""
        return f"{minutes:02d}:{seconds:02d}"

    @staticmethod
    def format_msc(minutes, seconds, centiseconds):
        """Formatea minutos, segundos y centésimas como MM:SS.CC."""
        return f"{minutes:02d}:{seconds:02d}.{centiseconds:02d}"

    @staticmethod
    def seconds_to_hms(total_seconds):
        """Convierte segundos totales a tupla (horas, minutos, segundos)."""
        hours = int(total_seconds) // 3600
        minutes = (int(total_seconds) % 3600) // 60
        seconds = int(total_seconds) % 60
        return hours, minutes, seconds

    @staticmethod
    def pad_number(number, digits=2):
        """Rellena un número con ceros a la izquierda."""
        return str(number).zfill(digits)

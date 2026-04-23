"""
Pantalla LCD - Componente que simula una pantalla LCD con dígitos de 7 segmentos.
Renderiza números al estilo de un reloj Casio real.
"""

from config.casio_theme import CasioTheme


class LCDDisplay:
    """
    Componente de pantalla LCD que dibuja dígitos de 7 segmentos
    sobre un Canvas de tkinter. Simula la apariencia real de un
    reloj digital Casio con segmentos activos e inactivos.
    """

    # Mapa de segmentos para cada dígito (a, b, c, d, e, f, g)
    # Disposición de segmentos:
    #   _a_
    #  f   b
    #   _g_
    #  e   c
    #   _d_
    DIGIT_MAP = {
        0: (1, 1, 1, 1, 1, 1, 0),
        1: (0, 1, 1, 0, 0, 0, 0),
        2: (1, 1, 0, 1, 1, 0, 1),
        3: (1, 1, 1, 1, 0, 0, 1),
        4: (0, 1, 1, 0, 0, 1, 1),
        5: (1, 0, 1, 1, 0, 1, 1),
        6: (1, 0, 1, 1, 1, 1, 1),
        7: (1, 1, 1, 0, 0, 0, 0),
        8: (1, 1, 1, 1, 1, 1, 1),
        9: (1, 1, 1, 1, 0, 1, 1),
    }

    def __init__(self, canvas):
        """Inicializa el componente LCD con referencia al canvas."""
        self._canvas = canvas
        self._light_on = False

    @property
    def segment_on_color(self):
        """Retorna el color de segmento activo según el modo de luz."""
        if self._light_on:
            return CasioTheme.SEGMENT_ON_LIGHT
        return CasioTheme.SEGMENT_ON

    @property
    def segment_off_color(self):
        """Retorna el color de segmento inactivo."""
        return CasioTheme.SEGMENT_OFF

    @property
    def lcd_bg_color(self):
        """Retorna el color de fondo LCD según el modo de luz."""
        if self._light_on:
            return CasioTheme.LCD_BG_LIGHT
        return CasioTheme.LCD_BG

    def set_light(self, on):
        """Activa o desactiva la iluminación LCD."""
        self._light_on = on

    def _get_segment_polygons(self, x, y, w, h, t):
        """
        Calcula los polígonos de los 7 segmentos de un dígito.

        Args:
            x, y: Posición superior izquierda del dígito.
            w: Ancho del dígito.
            h: Alto del dígito.
            t: Grosor de los segmentos.

        Returns:
            Lista de 7 listas de coordenadas (polígonos).
        """
        half_h = h / 2
        gap = 1  # Separación entre segmentos

        # Segmento a (horizontal superior)
        a = [
            x + t + gap, y,
            x + w - t - gap, y,
            x + w - t - gap - t // 2, y + t,
            x + t + gap + t // 2, y + t
        ]

        # Segmento b (vertical superior derecho)
        b = [
            x + w, y + t + gap,
            x + w, y + half_h - gap,
            x + w - t // 2, y + half_h,
            x + w - t, y + half_h - gap,
            x + w - t, y + t + gap
        ]

        # Segmento c (vertical inferior derecho)
        c = [
            x + w, y + half_h + gap,
            x + w, y + h - t - gap,
            x + w - t, y + h - t - gap,
            x + w - t, y + half_h + gap,
            x + w - t // 2, y + half_h
        ]

        # Segmento d (horizontal inferior)
        d = [
            x + t + gap + t // 2, y + h - t,
            x + w - t - gap - t // 2, y + h - t,
            x + w - t - gap, y + h,
            x + t + gap, y + h
        ]

        # Segmento e (vertical inferior izquierdo)
        e = [
            x, y + half_h + gap,
            x + t // 2, y + half_h,
            x + t, y + half_h + gap,
            x + t, y + h - t - gap,
            x, y + h - t - gap
        ]

        # Segmento f (vertical superior izquierdo)
        f = [
            x, y + t + gap,
            x + t, y + t + gap,
            x + t, y + half_h - gap,
            x + t // 2, y + half_h,
            x, y + half_h - gap
        ]

        # Segmento g (horizontal medio)
        g = [
            x + t + gap, y + half_h - t // 2,
            x + w - t - gap, y + half_h - t // 2,
            x + w - t - gap + t // 3, y + half_h,
            x + w - t - gap, y + half_h + t // 2,
            x + t + gap, y + half_h + t // 2,
            x + t + gap - t // 3, y + half_h
        ]

        return [a, b, c, d, e, f, g]

    def draw_digit(self, x, y, digit, size="large", tag=""):
        """
        Dibuja un dígito de 7 segmentos en la posición dada.

        Args:
            x, y: Posición superior izquierda.
            digit: Número a dibujar (0-9).
            size: "large" o "small" para el tamaño.
            tag: Tag para agrupar elementos en el canvas.
        """
        if size == "large":
            w = CasioTheme.SEGMENT_WIDTH_LARGE
            h = CasioTheme.SEGMENT_HEIGHT_LARGE
            t = CasioTheme.SEGMENT_THICKNESS_LARGE
        else:
            w = CasioTheme.SEGMENT_WIDTH_SMALL
            h = CasioTheme.SEGMENT_HEIGHT_SMALL
            t = CasioTheme.SEGMENT_THICKNESS_SMALL

        segments = self._get_segment_polygons(x, y, w, h, t)
        digit_segments = self.DIGIT_MAP.get(digit, (0, 0, 0, 0, 0, 0, 0))

        for i, (polygon, is_on) in enumerate(zip(segments, digit_segments)):
            color = self.segment_on_color if is_on else self.segment_off_color
            self._canvas.create_polygon(
                polygon,
                fill=color,
                outline="",
                tags=(tag, f"seg_{tag}_{i}")
            )

    def draw_number(self, x, y, number, digits=2, size="large", tag=""):
        """
        Dibuja un número con múltiples dígitos de 7 segmentos.

        Args:
            x, y: Posición superior izquierda.
            number: Número a dibujar.
            digits: Cantidad de dígitos a mostrar.
            size: "large" o "small".
            tag: Tag para el canvas.
        """
        if size == "large":
            w = CasioTheme.SEGMENT_WIDTH_LARGE
            spacing = w + 8
        else:
            w = CasioTheme.SEGMENT_WIDTH_SMALL
            spacing = w + 5

        num_str = str(number).zfill(digits)
        for i, ch in enumerate(num_str):
            self.draw_digit(x + i * spacing, y, int(ch), size, tag)

    def draw_colon(self, x, y, size="large", on=True, tag=""):
        """
        Dibuja los dos puntos (:) entre horas y minutos.

        Args:
            x, y: Posición del colon.
            size: "large" o "small".
            on: Si está visible o no (para efecto de parpadeo).
            tag: Tag para el canvas.
        """
        color = self.segment_on_color if on else self.segment_off_color

        if size == "large":
            dot_size = 4
            h = CasioTheme.SEGMENT_HEIGHT_LARGE
        else:
            dot_size = 3
            h = CasioTheme.SEGMENT_HEIGHT_SMALL

        # Punto superior
        cy1 = y + h // 3
        self._canvas.create_oval(
            x, cy1, x + dot_size, cy1 + dot_size,
            fill=color, outline="", tags=tag
        )

        # Punto inferior
        cy2 = y + 2 * h // 3
        self._canvas.create_oval(
            x, cy2, x + dot_size, cy2 + dot_size,
            fill=color, outline="", tags=tag
        )

    def draw_dot(self, x, y, size=4, on=True, tag=""):
        """Dibuja un punto (para separador de centésimas)."""
        color = self.segment_on_color if on else self.segment_off_color
        self._canvas.create_oval(
            x, y, x + size, y + size,
            fill=color, outline="", tags=tag
        )

    def draw_text(self, x, y, text, font=None, color=None, anchor="w", tag=""):
        """
        Dibuja texto en la pantalla LCD.

        Args:
            x, y: Posición del texto.
            text: Texto a mostrar.
            font: Fuente (por defecto LCD_LABEL).
            color: Color del texto.
            anchor: Anclaje del texto.
            tag: Tag para el canvas.
        """
        if font is None:
            font = CasioTheme.FONT_LCD_LABEL
        if color is None:
            color = self.segment_on_color

        self._canvas.create_text(
            x, y,
            text=text,
            font=font,
            fill=color,
            anchor=anchor,
            tags=tag
        )

    def clear(self, tag=""):
        """Elimina todos los elementos con el tag dado del canvas."""
        if tag:
            self._canvas.delete(tag)
        else:
            self._canvas.delete("lcd_content")

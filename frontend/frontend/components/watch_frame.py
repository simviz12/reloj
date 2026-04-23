"""
Caja Aeterna - Ingeniería de Precisión.
Diseño en acero quirúrgico pulido con brazalete integrado.
"""

import math
from config.casio_theme import CasioTheme


class WatchFrame:
    """
    Caja octogonal refinada con acabados en espejo y cepillado.
    Sustituye correas por un brazalete metálico de eslabones.
    """

    def __init__(self, canvas):
        self.canvas = canvas
        self.cx = CasioTheme.WINDOW_WIDTH // 2
        self.cy = CasioTheme.WINDOW_HEIGHT // 2

    def draw_watch_body(self):
        """Construye la caja y el brazalete."""
        r = CasioTheme.WATCH_SIZE // 2
        
        # 1. Caja Principal (Efecto Acero Pulido)
        self._draw_octagon(self.cx+10, self.cy+10, r, fill="#080808") # Sombra
        self._draw_octagon(self.cx, self.cy, r, fill=CasioTheme.STEEL_BRUSHED, outline="#111", width=2)
        
        # 2. Bisel Superior (Efecto Espejo)
        self._draw_octagon(self.cx, self.cy, r - 12, fill=CasioTheme.STEEL_POLISHED, outline="#aaa", width=1)
        
        # 3. Tornillos de Oro (Puntos de anclaje de lujo)
        screw_r = r - 25
        for i in range(8):
            a = math.radians(i * 45 + 22.5)
            self._draw_gold_bolt(self.cx + screw_r * math.sin(a), self.cy - screw_r * math.cos(a))

        # 4. Brazalete Integrado de Eslabones
        self._draw_metal_bracelet(self.cx, self.cy, r)

    def _draw_octagon(self, x, y, r, **kwargs):
        pts = []
        for i in range(8):
            a = math.radians(i * 45 + 22.5)
            pts.extend([x + r * math.sin(a), y - r * math.cos(a)])
        return self.canvas.create_polygon(pts, **kwargs)

    def _draw_gold_bolt(self, x, y):
        """Perno de oro pulido."""
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill=CasioTheme.GOLD_18K, outline=CasioTheme.GOLD_SOFT)
        self.canvas.create_oval(x-2, y-2, x+2, y+2, fill=CasioTheme.GOLD_SOFT, outline="")

    def _draw_metal_bracelet(self, cx, cy, r):
        """Brazalete de eslabones de acero cepillado."""
        for side in [-1, 1]:
            y_base = cy + side * (r - 10)
            direction = 1 if side == 1 else -1
            
            for i in range(5):
                y_pos = y_base + direction * (i * 35)
                w = 160 - i * 15
                h = 30
                
                # Eslabón
                self.canvas.create_rectangle(
                    cx - w//2, y_pos, cx + w//2, y_pos + direction * h,
                    fill=CasioTheme.STEEL_BRUSHED, outline="#666", width=1
                )
                # Detalle central pulido
                self.canvas.create_rectangle(
                    cx - w//4, y_pos, cx + w//4, y_pos + direction * h,
                    fill=CasioTheme.STEEL_POLISHED, outline="#999", width=1
                )

"""
Caja Aeterna - Edición Interactiva.
Incluye pulsadores físicos que responden al ratón.
"""

import math
from config.casio_theme import CasioTheme

class WatchFrame:
    def __init__(self, canvas):
        self.canvas = canvas
        self.cx = CasioTheme.WINDOW_WIDTH // 2
        self.cy = CasioTheme.WINDOW_HEIGHT // 2
        
        # Coordenadas de los botones para interacción
        self.buttons = {
            "ADJUST": (self.cx - 215, self.cy - 120),
            "MODE": (self.cx - 215, self.cy + 120),
            "LIGHT": (self.cx + 215, self.cy - 120),
            "START": (self.cx + 215, self.cy + 120)
        }

    def draw_watch_body(self):
        """Construye la caja, el brazalete y los pulsadores."""
        r = CasioTheme.WATCH_SIZE // 2
        
        # 1. Caja Principal
        self._draw_octagon(self.cx+10, self.cy+10, r, fill="#080808")
        self._draw_octagon(self.cx, self.cy, r, fill=CasioTheme.STEEL_BRUSHED, outline="#111", width=2)
        
        # 2. Pulsadores (Botones laterales)
        for name, pos in self.buttons.items():
            self._draw_pusher(pos[0], pos[1], "left" if pos[0] < self.cx else "right", name)

        # 3. Bisel Superior
        self._draw_octagon(self.cx, self.cy, r - 12, fill=CasioTheme.STEEL_POLISHED, outline="#aaa", width=1)
        
        # 4. Tornillos de Oro
        screw_r = r - 25
        for i in range(8):
            a = math.radians(i * 45 + 22.5)
            self._draw_gold_bolt(self.cx + screw_r * math.sin(a), self.cy - screw_r * math.cos(a))

        # 5. Brazalete
        self._draw_metal_bracelet(self.cx, self.cy, r)

    def _draw_pusher(self, x, y, side, name):
        """Dibuja un pulsador de acero."""
        w, h = 30, 50
        if side == "left":
            self.canvas.create_rectangle(x, y-h//2, x+20, y+h//2, fill="#555", outline="#222", tags="button")
            self.canvas.create_rectangle(x-5, y-h//2-5, x+15, y+h//2+5, fill=CasioTheme.STEEL_BRUSHED, outline="#111", tags=("button", name))
        else:
            self.canvas.create_rectangle(x-20, y-h//2, x, y+h//2, fill="#555", outline="#222", tags="button")
            self.canvas.create_rectangle(x-15, y-h//2-5, x+5, y+h//2+5, fill=CasioTheme.STEEL_BRUSHED, outline="#111", tags=("button", name))

    def _draw_octagon(self, x, y, r, **kwargs):
        pts = []
        for i in range(8):
            a = math.radians(i * 45 + 22.5)
            pts.extend([x + r * math.sin(a), y - r * math.cos(a)])
        return self.canvas.create_polygon(pts, **kwargs)

    def _draw_gold_bolt(self, x, y):
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill=CasioTheme.GOLD_18K, outline=CasioTheme.GOLD_SOFT)

    def _draw_metal_bracelet(self, cx, cy, r):
        for side in [-1, 1]:
            y_base = cy + side * (r - 10)
            direction = 1 if side == 1 else -1
            for i in range(5):
                y_pos = y_base + direction * (i * 35)
                w = 160 - i * 15
                h = 30
                self.canvas.create_rectangle(cx - w//2, y_pos, cx + w//2, y_pos + direction * h,
                                             fill=CasioTheme.STEEL_BRUSHED, outline="#666")

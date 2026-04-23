"""
Display Aeterna - Edición Realista.
Sincronizado perfectamente con la hora del sistema con movimiento de cuarzo (paso a paso).
"""

import math
from datetime import datetime
from config.casio_theme import CasioTheme

class AnalogDisplay:
    def __init__(self, canvas):
        self.canvas = canvas
        self.cx = CasioTheme.WINDOW_WIDTH // 2
        self.cy = CasioTheme.WINDOW_HEIGHT // 2

    def draw_face_static(self, theme):
        """Dibuja la esfera estática (solo cuando cambia el tema)."""
        self.canvas.delete("face_static")
        r = CasioTheme.DIAL_SIZE // 2
        
        # Fondo
        self.canvas.create_oval(self.cx-r, self.cy-r, self.cx+r, self.cy+r, 
                                fill=theme.dial, outline=theme.accent, width=2, tags="face_static")

        # Índices del 1 al 12
        for i in range(12):
            ang = math.radians(i * 30)
            # Marcadores
            x1 = self.cx + (r - 2) * math.sin(ang)
            y1 = self.cy - (r - 2) * math.cos(ang)
            x2 = self.cx + (r - 15) * math.sin(ang)
            y2 = self.cy - (r - 15) * math.cos(ang)
            self.canvas.create_line(x1, y1, x2, y2, fill=theme.accent, width=4, tags="face_static")
            
            # Números
            num = i if i > 0 else 12
            num_r = r - 45
            nx = self.cx + num_r * math.sin(ang)
            ny = self.cy - num_r * math.cos(ang)
            self.canvas.create_text(nx, ny, text=str(num), font=("Arial", 14, "bold"), fill=theme.hands, tags="face_static")

        # Logos
        self.canvas.create_text(self.cx, self.cy - 75, text="AETERNA", 
                                font=CasioTheme.FONT_BRAND, fill=theme.accent, tags="face_static")
        self.canvas.create_text(self.cx, self.cy + 130, text=theme.name, 
                                font=("Arial", 7, "bold"), fill=theme.accent, tags="face_static")

    def draw_date_window(self, theme, day):
        self.canvas.delete("date_window")
        r = CasioTheme.DIAL_SIZE // 2
        self.canvas.create_rectangle(self.cx+r-75, self.cy-15, self.cx+r-35, self.cy+15, 
                                     fill=theme.hands, outline=theme.accent, width=2, tags="date_window")
        self.canvas.create_text(self.cx+r-55, self.cy, text=str(day), 
                                font=("Arial", 12, "bold"), fill="#000", tags="date_window")

    def draw_hands(self, theme, h, m, s):
        """Dibuja las manecillas con movimiento de reloj normal (por segundos)."""
        self.canvas.delete("hands")
        
        # Ángulos precisos
        h_ang = math.radians((h % 12) * 30 + m * 0.5)
        m_ang = math.radians(m * 6)
        s_ang = math.radians(s * 6) # Movimiento por segundo exacto

        # Manecillas Horas (Blanco)
        self._draw_dauphine_hand(h_ang, 95, 12, "#ffffff")
        # Manecillas Minutos (Blanco)
        self._draw_dauphine_hand(m_ang, 140, 10, "#ffffff")
        
        # Segundero (Color acento del tema - Oro por defecto)
        self.canvas.create_line(
            self.cx - 35 * math.sin(s_ang), self.cy + 35 * math.cos(s_ang),
            self.cx + 155 * math.sin(s_ang), self.cy - 155 * math.cos(s_ang),
            fill="#d4af37", width=2, tags="hands"
        )
        
        # Pin central
        self.canvas.create_oval(self.cx-8, self.cy-8, self.cx+8, self.cy+8, fill="#222", outline=theme.accent, tags="hands")

    def _draw_dauphine_hand(self, angle, length, width, color):
        hw = width / 2
        pts1 = [self.cx, self.cy, self.cx + length * math.sin(angle), self.cy - length * math.cos(angle),
                self.cx + hw * math.sin(angle + 1.57), self.cy - hw * math.cos(angle + 1.57)]
        pts2 = [self.cx, self.cy, self.cx + length * math.sin(angle), self.cy - length * math.cos(angle),
                self.cx + hw * math.sin(angle - 1.57), self.cy - hw * math.cos(angle - 1.57)]
        self.canvas.create_polygon(pts1, fill="#ffffff", outline="", tags="hands")
        self.canvas.create_polygon(pts2, fill="#cccccc", outline="", tags="hands")

    def draw_glass_effects(self):
        r = CasioTheme.DIAL_SIZE // 2
        self.canvas.create_oval(self.cx-r, self.cy-r, self.cx+r, self.cy+r, 
                                outline="#ffffff", width=1, stipple="gray12", tags="glass")

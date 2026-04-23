"""
Display Aeterna - Masterpiece Edition.
Esfera con soporte para temas dinámicos.
"""

import math
from config.casio_theme import CasioTheme

class AnalogDisplay:
    def __init__(self, canvas):
        self.canvas = canvas
        self.cx = CasioTheme.WINDOW_WIDTH // 2
        self.cy = CasioTheme.WINDOW_HEIGHT // 2
        self.gear_angle = 0

    def draw_face_themed(self, theme):
        """Dibuja la esfera usando los colores del tema proporcionado."""
        r = CasioTheme.DIAL_SIZE // 2
        
        # 1. Fondo del Dial
        self.canvas.create_oval(self.cx-r, self.cy-r, self.cx+r, self.cy+r, 
                                fill=theme.dial, outline=theme.accent, width=2, tags="face")

        # 2. Efecto Sunburst
        for i in range(0, 360, 15):
            ang = math.radians(i)
            self.canvas.create_line(
                self.cx, self.cy,
                self.cx + (r-5) * math.sin(ang),
                self.cy - (r-5) * math.cos(ang),
                fill=theme.accent, width=1, stipple="gray25", tags=("face", "dynamic")
            )

        # 3. Índices y Números
        for i in range(12):
            ang = math.radians(i * 30)
            x1 = self.cx + (r - 2) * math.sin(ang)
            y1 = self.cy - (r - 2) * math.cos(ang)
            x2 = self.cx + (r - 15) * math.sin(ang)
            y2 = self.cy - (r - 15) * math.cos(ang)
            self.canvas.create_line(x1, y1, x2, y2, fill=theme.accent, width=4, tags="face")
            
            num = i if i > 0 else 12
            num_r = r - 45
            nx = self.cx + num_r * math.sin(ang)
            ny = self.cy - num_r * math.cos(ang)
            self.canvas.create_text(nx, ny, text=str(num), font=("Arial", 14, "bold"), fill=theme.hands, tags="face")

        # 4. Branding
        self.canvas.create_text(self.cx, self.cy - 75, text="AETERNA", 
                                font=CasioTheme.FONT_BRAND, fill=theme.accent, tags="face")
        self.canvas.create_text(self.cx, self.cy + 130, text=theme.name, 
                                font=("Arial", 7, "bold"), fill=theme.accent, tags="face")

        # 5. Ventana de fecha
        self._draw_date_window_themed(theme)

    def _draw_date_window_themed(self, theme):
        r = CasioTheme.DIAL_SIZE // 2
        from datetime import datetime
        day = datetime.now().day
        self.canvas.create_rectangle(self.cx+r-75, self.cy-15, self.cx+r-35, self.cy+15, 
                                     fill=theme.hands, outline=theme.accent, width=2, tags="face")
        self.canvas.create_text(self.cx+r-55, self.cy, text=str(day), 
                                font=("Arial", 12, "bold"), fill="#000", tags="face")

    def draw_hands(self, h, m, s):
        self.canvas.delete("hands")
        h_ang = math.radians((h % 12) * 30 + m * 0.5)
        m_ang = math.radians(m * 6 + s * 0.1)
        s_ang = math.radians(s * 6)

        self._draw_dauphine_hand(h_ang, 95, 12, "#ffffff")
        self._draw_dauphine_hand(m_ang, 140, 10, "#ffffff")
        
        # Segundero
        self.canvas.create_line(
            self.cx - 35 * math.sin(s_ang), self.cy + 35 * math.cos(s_ang),
            self.cx + 155 * math.sin(s_ang), self.cy - 155 * math.cos(s_ang),
            fill="#d4af37", width=2, tags="hands"
        )

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
                                outline="#ffffff", width=1, stipple="gray12", tags="face")
        self.canvas.create_arc(self.cx-r+20, self.cy-r+20, self.cx+r-20, self.cy+r-20, 
                               start=100, extent=60, style="arc", outline="#ffffff", width=2, tags="face")

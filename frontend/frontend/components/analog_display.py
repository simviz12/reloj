"""
Display Aeterna - Masterpiece Edition.
Esfera con efecto Sunburst, índices aplicados a mano y segundero continuo.
"""

import math
from config.casio_theme import CasioTheme


class AnalogDisplay:
    """
    Motor de renderizado para la esfera Aeterna. 
    Simula reflejos de luz radiales y profundidad de cristal de zafiro.
    """

    def __init__(self, canvas):
        self.canvas = canvas
        self.cx = CasioTheme.WINDOW_WIDTH // 2
        self.cy = CasioTheme.WINDOW_HEIGHT // 2
        self.gear_angle = 0

    def draw_face(self, seconds):
        """Dibuja la esfera esmeralda con efecto sunburst dinámico."""
        r = CasioTheme.DIAL_SIZE // 2
        
        # 1. Efecto Sunburst (Fondo dinámico)
        self.canvas.delete("sunburst")
        offset = (seconds * 0.5) % 360
        
        for i in range(0, 360, 1):
            ang = math.radians(i + offset)
            color = self._get_sunburst_color(i)
            # Dibujamos un poco más corto para que no toque el borde del oro
            self.canvas.create_line(
                self.cx, self.cy,
                self.cx + (r-2) * math.sin(ang),
                self.cy - (r-2) * math.cos(ang),
                fill=color, width=4, tags=("face", "sunburst")
            )

        # 2. Engranajes (Skeleton parcial bajo el dial)
        self._draw_gears(self.cx, self.cy + 75, 45)

        # 4. Índices y Números (TODOS DEL 1 AL 12)
        for i in range(12):
            ang = math.radians(i * 30)
            # Marcador Baton
            x1 = self.cx + (r - 2) * math.sin(ang)
            y1 = self.cy - (r - 2) * math.cos(ang)
            x2 = self.cx + (r - 15) * math.sin(ang)
            y2 = self.cy - (r - 15) * math.cos(ang)
            self.canvas.create_line(x1, y1, x2, y2, fill=CasioTheme.GOLD_18K, width=4, tags="face")
            
            # Número (1-12)
            num = i if i > 0 else 12
            num_r = r - 45
            nx = self.cx + num_r * math.sin(ang)
            ny = self.cy - num_r * math.cos(ang)
            self.canvas.create_text(nx, ny, text=str(num), font=("Arial", 14, "bold"), fill="#ffffff", tags="face")

        # 5. Branding (Reposicionado para evitar solapamientos)
        self.canvas.create_text(self.cx, self.cy - 75, text="AETERNA", 
                                font=CasioTheme.FONT_BRAND, fill=CasioTheme.GOLD_SOFT, tags="face")
        self.canvas.create_text(self.cx, self.cy - 52, text="CRONÓMETRO", 
                                font=("Helvetica", 7, "bold"), fill="#ffffff", tags="face")
        self.canvas.create_text(self.cx, self.cy + 130, text="SWISS MADE", 
                                font=("Arial", 7, "bold"), fill="#aaaaaa", tags="face")

        # 5. Ventana de fecha
        self._draw_date_window()

    def _get_sunburst_color(self, angle):
        """Genera un degradado de verde esmeralda más suave y elegante."""
        # Variación más sutil
        brightness = int(15 + 15 * abs(math.cos(math.radians(angle * 1.5))))
        return f"#06{brightness:02x}1a"

    def _draw_gears(self, x, y, r):
        """Simulación de maquinaria con metales de lujo."""
        self.canvas.delete("gears")
        self.gear_angle += 2
        
        # Engranaje Grande (Oro Viejo)
        self._draw_single_gear(x, y, r, self.gear_angle, "#9a7b4f")
        # Engranaje Pequeño (Oro 18k)
        self._draw_single_gear(x + r + 5, y, r // 2, -self.gear_angle * 2, CasioTheme.GOLD_18K)

    def _draw_date_window(self):
        """Ventana de fecha con marco de oro."""
        r = CasioTheme.DIAL_SIZE // 2
        from datetime import datetime
        day = datetime.now().day
        
        # Marco
        self.canvas.create_rectangle(self.cx+r-75, self.cy-15, self.cx+r-35, self.cy+15, 
                                     fill="#ffffff", outline=CasioTheme.GOLD_18K, width=2, tags="face")
        # Número
        self.canvas.create_text(self.cx+r-55, self.cy, text=str(day), 
                                font=("Arial", 12, "bold"), fill="#000", tags="face")

    def _draw_single_gear(self, x, y, r, angle_offset, color):
        """Dibuja un engranaje con dientes reales."""
        points = []
        teeth = 12
        for i in range(teeth * 2):
            angle = math.radians(i * (360 / (teeth * 2)) + angle_offset)
            dist = r if i % 2 == 0 else r + 8
            points.extend([x + dist * math.sin(angle), y - dist * math.cos(angle)])
        
        self.canvas.create_polygon(points, fill=color, outline="#222222", tags="gears")
        self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="#111111", outline="", tags="gears")

    def draw_hands(self, h, m, s):
        """Manecillas 'Dauphine' en platino y oro."""
        self.canvas.delete("hands")
        
        h_ang = math.radians((h % 12) * 30 + m * 0.5)
        m_ang = math.radians(m * 6 + s * 0.1)
        s_ang = math.radians(s * 6)

        # 1. Horas y Minutos (Estilo Dauphine con bisel central)
        self._draw_dauphine_hand(h_ang, 95, 12, CasioTheme.STEEL_POLISHED)
        self._draw_dauphine_hand(m_ang, 140, 10, CasioTheme.STEEL_POLISHED)
        
        # 2. Segundero "Lollipop" en oro
        self.canvas.create_line(
            self.cx - 35 * math.sin(s_ang), self.cy + 35 * math.cos(s_ang),
            self.cx + 155 * math.sin(s_ang), self.cy - 155 * math.cos(s_ang),
            fill=CasioTheme.GOLD_18K, width=2, tags="hands"
        )
        # Círculo segundero
        sx = self.cx + 120 * math.sin(s_ang)
        sy = self.cy - 120 * math.cos(s_ang)
        self.canvas.create_oval(sx-5, sy-5, sx+5, sy+5, fill=CasioTheme.GOLD_18K, outline="#000", tags="hands")

        # Pin central
        self.canvas.create_oval(self.cx-8, self.cy-8, self.cx+8, self.cy+8, fill="#222", outline=CasioTheme.GOLD_18K, tags="hands")

    def _draw_dauphine_hand(self, angle, length, width, color):
        """Manecilla triangular con pliegue central para efecto 3D."""
        hw = width / 2
        # Lado Luz
        pts1 = [self.cx, self.cy, self.cx + length * math.sin(angle), self.cy - length * math.cos(angle),
                self.cx + hw * math.sin(angle + 1.57), self.cy - hw * math.cos(angle + 1.57)]
        # Lado Sombra
        pts2 = [self.cx, self.cy, self.cx + length * math.sin(angle), self.cy - length * math.cos(angle),
                self.cx + hw * math.sin(angle - 1.57), self.cy - hw * math.cos(angle - 1.57)]
        
        self.canvas.create_polygon(pts1, fill="#ffffff", outline="", tags="hands")
        self.canvas.create_polygon(pts2, fill="#cccccc", outline="", tags="hands")

    def draw_glass_effects(self):
        """Simulación de cristal de zafiro con recubrimiento AR (Anti-Reflectante)."""
        r = CasioTheme.DIAL_SIZE // 2
        # Brillo azulado sutil en el borde
        self.canvas.create_oval(self.cx-r, self.cy-r, self.cx+r, self.cy+r, 
                                outline="#4466ff", width=1, stipple="gray12", tags="face")
        # Reflejo principal
        self.canvas.create_arc(self.cx-r+20, self.cy-r+20, self.cx+r-20, self.cy+r-20, 
                               start=100, extent=60, style="arc", outline="#ffffff", width=2, tags="face")

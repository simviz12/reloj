"""
Modelo de Temas - Define las paletas de colores para la personalización del reloj.
"""

class Theme:
    def __init__(self, name, dial, hands, accent, lcd_bg, text):
        self.name = name
        self.dial = dial
        self.hands = hands
        self.accent = accent
        self.lcd_bg = lcd_bg
        self.text = text

class ThemeManager:
    """Gestiona los temas disponibles usando una Lista Circular Doble."""
    def __init__(self):
        from .circular_list import CircularDoubleLinkedList
        self.themes = CircularDoubleLinkedList()
        
        # Tema 1: Esmeralda Real (Original)
        self.themes.append(Theme(
            "ESMERALDA REAL",
            dial="#062a1a", hands="#ffffff", accent="#d4af37",
            lcd_bg="#7a8a7a", text="#1a1a1a"
        ))
        
        # Tema 2: Platino Ártico (Azul y Plata)
        self.themes.append(Theme(
            "PLATINO ÁRTICO",
            dial="#0a1a2a", hands="#f0f0f5", accent="#a0b0ff",
            lcd_bg="#7a808a", text="#051020"
        ))
        
        # Tema 3: Obsidiana (Negro y Gris)
        self.themes.append(Theme(
            "OBSIDIANA",
            dial="#050505", hands="#c0c0c0", accent="#606060",
            lcd_bg="#404040", text="#000000"
        ))

    def next_theme(self):
        return self.themes.next()

    def get_current(self):
        return self.themes.get_current()

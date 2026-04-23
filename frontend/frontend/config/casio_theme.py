"""
Tema Aeterna - Edición Esmeralda y Platino.
Un diseño de alta relojería que trasciende lo convencional.
"""


class CasioTheme:
    """
    Paleta de colores: Verde Esmeralda Sunburst, Acero Quirúrgico y Oro de 18k.
    """

    # --- Ventana ---
    WINDOW_WIDTH = 550
    WINDOW_HEIGHT = 800
    WINDOW_TITLE = "AETERNA - Haute Horlogerie"

    # --- Metales ---
    STEEL_POLISHED = "#f0f0f5"
    STEEL_BRUSHED = "#c0c0c8"
    GOLD_18K = "#d4af37"
    GOLD_SOFT = "#f1e5ac"

    # --- Dial ---
    DIAL_EMERALD = "#062a1a"         # Centro profundo
    DIAL_SUNBURST = "#0a4d32"        # Reflejo radial
    
    # --- Manecillas ---
    HAND_MAIN = "#ffffff"            # Acero pulido
    HAND_ACCENT = "#d4af37"          # Detalles en oro
    LUME_GLOW = "#50ff50"            # Verde radioactivo

    # --- Dimensiones ---
    WATCH_SIZE = 430
    DIAL_SIZE = 320

    # --- Fuentes ---
    FONT_BRAND = ("Garamond", 22, "bold")
    FONT_MODEL = ("Arial Narrow", 9, "bold")
    FONT_NUM = ("Century Gothic", 13, "bold")
    
    # --- LCD Constants (Digital Modes) ---
    LCD_BG = "#7a8a7a"
    LCD_BG_LIGHT = "#a0b0a0"
    SEGMENT_ON = "#1a1a1a"
    SEGMENT_ON_LIGHT = "#0a0a0a"
    SEGMENT_OFF = "#6a7a6a"
    
    LCD_WIDTH = 260
    LCD_HEIGHT = 160
    LCD_X = (WINDOW_WIDTH - LCD_WIDTH) // 2
    LCD_Y = 320
    LCD_PADDING = 10

    SEGMENT_WIDTH_LARGE = 25
    SEGMENT_HEIGHT_LARGE = 45
    SEGMENT_THICKNESS_LARGE = 6
    
    SEGMENT_WIDTH_SMALL = 15
    SEGMENT_HEIGHT_SMALL = 25
    SEGMENT_THICKNESS_SMALL = 4

    FONT_LCD_LABEL = ("Consolas", 10, "bold")
    FONT_LCD_SMALL = ("Consolas", 8, "bold")
    FONT_MODE = ("Consolas", 12, "bold")

    # --- Mode Names ---
    MODE_CLOCK = "HORA"
    MODE_ALARM = "ALARMA"
    MODE_STOPWATCH = "CRONO"
    MODE_TIMER = "TIMER"

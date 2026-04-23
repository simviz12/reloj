"""
AETERNA Haute Horlogerie - Emerald & Platinum Edition.
"""

import sys
import os
import tkinter as tk

_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(_root, "backend", "backend"))

from config.casio_theme import CasioTheme
from components.analog_display import AnalogDisplay
from components.watch_frame import WatchFrame

class Clockwork:
    from datetime import datetime
    def time(self):
        n = self.datetime.now()
        return {"h": n.hour, "m": n.minute, "s": n.second, "ms": n.microsecond // 1000}

class AeternaApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(CasioTheme.WINDOW_TITLE)
        self.root.geometry("550x800")
        self.root.configure(bg="#010305")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=550, height=800, bg="#010305", highlightthickness=0)
        self.canvas.pack()

        self.engine = Clockwork()
        self.display = AnalogDisplay(self.canvas)
        self.frame = WatchFrame(self.canvas)
        
        self.setup()
        self.refresh()

    def setup(self):
        self.canvas.delete("all")
        
        # 1. Fondo de Madera de Lujo (Mahogany)
        self.canvas.create_rectangle(0, 0, 550, 800, fill="#1a0f00", outline="")
        # Textura de vetas de madera
        for i in range(0, 800, 4):
            opacity = (i % 40) // 4
            color = f"#{20+opacity:02x}{12+opacity:02x}{0:02x}"
            self.canvas.create_line(0, i, 550, i, fill=color, width=2)

        # 2. Sombra Proyectada del Reloj Completo
        self.canvas.create_oval(75, 100, 475, 700, fill="#0a0600", outline="", stipple="gray25")
        
        self.frame.draw_watch_body()

    def refresh(self):
        t = self.engine.time()
        self.canvas.delete("dynamic")
        
        # Renderizado de precisión
        self.display.draw_face(t["s"] + t["ms"]/1000)
        self.display.draw_hands(t["h"], t["m"], t["s"])
        self.display.draw_glass_effects()
        
        self.root.after(30, self.refresh)

if __name__ == "__main__":
    AeternaApp().root.mainloop()

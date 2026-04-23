"""
CasioWatchApp - Versión Realista.
Sincronización total entre el backend de tiempo y el frontend analógico/digital.
"""

import sys
import os
import tkinter as tk
from datetime import datetime

_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(_root, "backend", "backend"))

from config.casio_theme import CasioTheme
from components.analog_display import AnalogDisplay
from components.lcd_display import LCDDisplay
from components.watch_frame import WatchFrame

from services.clock_service import ClockService
from services.alarm_service import AlarmService
from services.stopwatch_service import StopwatchService
from services.timer_service import TimerService

from views.clock_view import ClockView
from views.alarm_view import AlarmView
from views.stopwatch_view import StopwatchView
from views.timer_view import TimerView

from models.circular_list import CircularDoubleLinkedList
from models.themes import ThemeManager

class CasioWatchApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(CasioTheme.WINDOW_TITLE)
        self.root.geometry("550x800")
        self.root.configure(bg="#010305")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=550, height=800, bg="#010305", highlightthickness=0)
        self.canvas.pack()

        self.theme_manager = ThemeManager()
        self.analog_display = AnalogDisplay(self.canvas)
        self.lcd_display = LCDDisplay(self.canvas)
        self.frame = WatchFrame(self.canvas)

        self.services = {
            "clock": ClockService(), "alarm": AlarmService(),
            "stopwatch": StopwatchService(), "timer": TimerService()
        }

        self.views = {
            "clock": ClockView(self.analog_display, self.services["clock"]),
            "alarm": AlarmView(self.lcd_display, self.services["alarm"]),
            "stopwatch": StopwatchView(self.lcd_display, self.services["stopwatch"]),
            "timer": TimerView(self.lcd_display, self.services["timer"])
        }

        self.mode_selector = CircularDoubleLinkedList()
        for v in ["clock", "alarm", "stopwatch", "timer"]:
            self.mode_selector.append(self.views[v])

        self._last_theme = None
        self._last_day = None
        
        self.setup_ui()
        self.bind_controls()
        self.run_loop()

    def setup_ui(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 550, 800, fill="#1a0f00", outline="")
        for i in range(0, 800, 4):
            c = f"#{20+(i%40)//4:02x}{12+(i%40)//4:02x}00"
            self.canvas.create_line(0, i, 550, i, fill=c)
        self.frame.draw_watch_body()

    def bind_controls(self):
        self.root.bind("<Return>", lambda e: self.next_mode())
        self.root.bind("<BackSpace>", lambda e: self.prev_mode())
        self.root.bind("<t>", lambda e: self.change_theme())
        self.root.bind("<space>", lambda e: self.current_view().on_start_stop())
        self.root.bind("<r>", lambda e: self.current_view().on_reset())
        self.root.bind("<a>", lambda e: self.current_view().on_adjust())
        self.root.bind("<l>", lambda e: self.toggle_light())
        
        self.canvas.tag_bind("MODE", "<Button-1>", lambda e: self.next_mode())
        self.canvas.tag_bind("ADJUST", "<Button-1>", lambda e: self.current_view().on_adjust())
        self.canvas.tag_bind("LIGHT", "<Button-1>", lambda e: self.toggle_light())
        self.canvas.tag_bind("START", "<Button-1>", lambda e: self.current_view().on_start_stop())

    def current_view(self):
        return self.mode_selector.get_current()

    def change_theme(self):
        self.theme_manager.next_theme()
        self._last_theme = None

    def next_mode(self):
        self.mode_selector.next()
        self.lcd_display.clear("lcd_content")

    def prev_mode(self):
        self.mode_selector.prev()
        self.lcd_display.clear("lcd_content")

    def toggle_light(self):
        self.lcd_display.set_light(not self.lcd_display._light_on)

    def run_loop(self):
        self.canvas.delete("dynamic")
        theme = self.theme_manager.get_current()
        active = self.current_view()
        
        # 1. Elementos estáticos
        if self._last_theme != theme:
            self.analog_display.draw_face_static(theme)
            self._last_theme = theme
            self.analog_display.draw_glass_effects()
        
        # 2. Tiempo real desde el sistema
        now = datetime.now()
        
        # 3. Actualizar fecha
        if self._last_day != now.day:
            self.analog_display.draw_date_window(theme, now.day)
            self._last_day = now.day

        # 4. Renderizar Manecillas (Siempre activas en fondo o principal)
        # Usamos los datos reales del sistema para evitar que "vaya rápido"
        self.analog_display.draw_hands(theme, now.hour, now.minute, now.second)

        # 5. Renderizar Vista (Si no es el reloj principal, dibujar LCD encima)
        if not isinstance(active, ClockView):
            lx, ly = CasioTheme.LCD_X, CasioTheme.LCD_Y
            lw, lh = CasioTheme.LCD_WIDTH, CasioTheme.LCD_HEIGHT
            bg = theme.lcd_bg if not self.lcd_display._light_on else CasioTheme.LCD_BG_LIGHT
            self.canvas.create_rectangle(lx, ly, lx+lw, ly+lh, fill=bg, outline=theme.accent, width=2, tags="dynamic")
            if self.lcd_display._light_on:
                self.canvas.create_rectangle(lx-3, ly-3, lx+lw+3, ly+lh+3, outline=theme.accent, width=1, tags="dynamic")
            active.render()

        self.root.after(100, self.run_loop) # Reducimos frecuencia de actualización para estabilidad

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    CasioWatchApp().run()

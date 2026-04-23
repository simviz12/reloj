"""
Punto de Entrada Principal - Ejecuta la aplicación del Reloj Casio Digital.

Este archivo es el punto de entrada del frontend.
Inicializa y ejecuta la aplicación completa del reloj.

Uso:
    python main.py

Controles:
    - LIGHT:     Iluminar pantalla (tecla L)
    - MODE:      Cambiar modo (tecla Enter)
    - ST/SP:     Iniciar/Parar (tecla Espacio)
    - RESET:     Reiniciar (tecla R)
    - ADJUST:    Ajustar (tecla A)

Modos disponibles:
    1. HORA    - Reloj principal con hora, fecha y día
    2. ALARMA  - Configuración de alarma
    3. CRONO   - Cronómetro con vueltas
    4. TIMER   - Temporizador con cuenta regresiva
"""

import sys
import os

# Configurar el path para importaciones relativas
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from app import CasioWatchApp


def main():
    """Función principal que crea y ejecuta la aplicación."""
    print("=" * 50)
    print("  CASIO Digital Watch - Python Edition")
    print("=" * 50)
    print()
    print("  Controles del teclado:")
    print("    L     - Iluminar pantalla")
    print("    Enter - Cambiar modo")
    print("    Space - Iniciar/Parar")
    print("    R     - Reiniciar")
    print("    A     - Ajustar")
    print()
    print("  Modos: HORA | ALARMA | CRONO | TIMER")
    print("=" * 50)

    app = CasioWatchApp()
    app.run()


if __name__ == "__main__":
    main()

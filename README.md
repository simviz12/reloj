# AETERNA Masterpiece - Taller de Estructuras de Datos

## 💎 El Proyecto
AETERNA es una simulación de alta fidelidad de un reloj de lujo que integra conceptos avanzados de programación y estructuras de datos. Esta versión ha sido desarrollada específicamente para el **Taller de Listas Circulares Dobles**, demostrando su utilidad práctica en sistemas de navegación de interfaces.

## 🏗️ Innovaciones Técnicas (Requerimientos del Taller)

### 1. Lista Circular Doblemente Enlazada (Modos)
El sistema de navegación principal del reloj utiliza una **Lista Circular Doble**.
- **Circularidad:** Permite ciclar infinitamente entre los modos (Reloj -> Alarma -> Crono -> Timer -> Reloj).
- **Bidireccionalidad:** Gracias a los punteros `prev` y `next`, el usuario puede avanzar (`Enter`) o retroceder (`Backspace`) en los modos.
- **Implementación:** Se encuentra en `backend/backend/models/circular_list.py`.

### 2. Selector de Temas Dinámicos (Funcionalidad Extra)
Se implementó una **segunda Lista Circular Doble** para gestionar la personalización estética.
- **Temas:** Esmeralda Real, Platino Ártico y Obsidiana.
- **Uso:** Permite cambiar la paleta de colores completa en tiempo real sin perder el estado del reloj.

## 🎨 Características del Frontend
- **Renderizado Procedimental:** Dibujo dinámico de manecillas y esferas con `tkinter.Canvas`.
- **Interacción Híbrida:** 
    - **Teclado:** Control total mediante teclas rápidas.
    - **Ratón (Pulsadores):** Interacción táctil con los botones físicos laterales del reloj.
- **Movimiento de Cuarzo:** Sincronización precisa con el reloj del sistema.

## ⌨️ Controles de Usuario
| Acción | Teclado | Ratón (Clic) |
| :--- | :--- | :--- |
| **Siguiente Modo** | `Enter` | Botón Inferior Izquierdo |
| **Modo Anterior** | `Backspace` | - |
| **Cambiar Tema** | `T` | - |
| **Iniciar / Parar** | `Espacio` | Botón Inferior Derecho |
| **Reiniciar (Reset)** | `R` | - |
| **Ajustar (Adjust)** | `A` | Botón Superior Izquierdo |
| **Luz (Light)** | `L` | Botón Superior Derecho |

## 🚀 Ejecución
```bash
cd frontend/frontend
python main.py
```

---
*Desarrollo Profesional - Taller de Programación Python - Abril 2026*

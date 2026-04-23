# AETERNA - Haute Horlogerie (Edición Masterpiece)

## 💎 El Proyecto
AETERNA es una simulación de alta fidelidad de un reloj de lujo de gran complicación, desarrollado íntegramente en **Python**. El proyecto ha evolucionado desde un concepto digital hasta convertirse en una pieza de ingeniería visual que emula los materiales y la mecánica de la alta relojería suiza.

## 🌟 Características Destacadas
- **Diseño de Caja "Grand Royal":** Carcasa octogonal de acero quirúrgico pulido con tornillos de oro de 18k.
- **Esfera Esmeralda Sunburst:** Dial dinámico que reacciona al tiempo con reflejos radiales de luz.
- **Movimiento Skeleton:** Maquinaria interna (engranajes) animada que simula el corazón mecánico del reloj.
- **Brazalete Integrado:** Sistema de eslabones metálicos detallados con acabados bitonales.
- **Presentación de Lujo:** Fondo de madera de caoba (Mahogany) texturizado para un contexto de exhibición.
- **Precisión Suiza:** Motor de tiempo sincronizado con el sistema y renderizado a 30 FPS para una fluidez total.

## 🏗️ Arquitectura del Software
El sistema está dividido en dos grandes bloques para garantizar la mantenibilidad y escalabilidad:

### 1. Backend (`/backend`)
Gestiona la "inteligencia" del reloj. 
- **Modelos:** Clases puras de Python que calculan el tiempo, gestionan alarmas y estados internos sin depender de la interfaz gráfica.

### 2. Frontend (`/frontend`)
Gestiona la "estética" y el renderizado.
- **Configuración:** Sistema de temas centralizado para colores, fuentes y dimensiones.
- **Componentes:** Clases especializadas en dibujo geométrico complejo (Trigonometría para manecillas y engranajes).
- **Orquestador (`app.py`):** El motor principal que une la lógica con la visualización.

## 🚀 Ejecución Rápida
```bash
cd frontend/frontend
python app.py
```

---
*Proyecto desarrollado para el Taller de Programación en Python - Abril 2026.*

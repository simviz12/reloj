# Frontend - Interfaz de Alta Relojería

## 🎨 Visuales de Alta Fidelidad
El frontend del proyecto AETERNA utiliza el módulo `tkinter.Canvas` para realizar un renderizado procedimental de alta complejidad, simulando materiales físicos y efectos ópticos.

## 📐 Desafíos Técnicos Superados
- **Trigonometría Avanzada:** Cálculo de ángulos para manecillas, engranajes y el efecto Sunburst mediante funciones `sin` y `cos`.
- **Efectos de Materiales:** 
    - **Brushed Steel:** Uso de polígonos con degradados de gris.
    - **Sunburst Emerald:** Dibujo de cientos de líneas con variaciones de color radiales.
    - **Antialiasing manual:** Técnicas de dibujo para suavizar bordes en un entorno de canvas básico.
- **Sincronización a 30 FPS:** Optimización del bucle `after` de tkinter para mantener una animación fluida sin saturar el procesador.

## 📂 Componentes Clave
- `config/casio_theme.py`: Definición de la identidad visual (Aeterna Style).
- `components/analog_display.py`: Motor de renderizado de la esfera, manecillas y engranajes.
- `components/watch_frame.py`: Modelado de la caja octogonal y el brazalete metálico.
- `app.py`: El "Glue Code" que integra el fondo de madera, la iluminación y la actualización constante.

## ⌨️ Interacción
- El reloj se actualiza automáticamente.
- El diseño está optimizado para una visualización HD en pantallas modernas.

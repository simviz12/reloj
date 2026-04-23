# Backend - Motor de Tiempo Aeterna

## ⚙️ Lógica de Precisión
El backend constituye el núcleo de procesamiento del reloj. Su función es proporcionar datos precisos y estructurados al frontend, abstrayendo la complejidad del manejo de fechas y cálculos temporales.

## 📁 Estructura Interna
- `models/clock.py`: Gestiona la hora actual, fecha y formatos. Proporciona diccionarios de datos listos para ser consumidos por la UI.
- `models/alarm.py`: Lógica de comparación temporal para el sistema de alertas.
- `models/stopwatch.py`: Manejo de cronometría con precisión de milisegundos.
- `models/timer.py`: Lógica de cuenta regresiva y estados de finalización.

## 🛠️ Tecnologías
- **Python Standard Library:** Uso intensivo de `datetime` y `time`.
- **Arquitectura desacoplada:** El backend no conoce la existencia de `tkinter` ni de la interfaz, lo que permite su reutilización en otros entornos (web, móvil, consola).

## 🧩 Patrones Aplicados
- **Singleton/Service:** Gestión única del estado del tiempo.
- **Encapsulamiento:** Protección de los estados internos de los motores de cronometría.

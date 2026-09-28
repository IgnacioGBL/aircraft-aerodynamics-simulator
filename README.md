# Aircraft Aerodynamics & Performance Simulator

Aplicación de escritorio en Python para analizar aerodinámica y prestaciones básicas de un avión: sustentación, resistencia, peso, velocidad de pérdida y ratio L/D, con visualización mediante gráficas.

Proyecto personal de aprendizaje, desarrollado progresivamente mientras aprendo Python y conceptos de ingeniería aeroespacial.

## Estado actual

🚧 En desarrollo — Nivel 3 (cálculos vectorizados con NumPy + gráficas con Matplotlib)

## Funcionalidades implementadas

- Cálculo de Lift, Drag, Weight, velocidad de pérdida y ratio L/D (`calculations.py`)
- Cálculo vectorizado con NumPy sobre rangos de velocidades y ángulos de ataque
- Gráficas: Lift vs Airspeed, Drag vs Airspeed

## Próximos pasos

- [ ] Gráfica L/D vs Angle of Attack
- [ ] Modelar el ángulo de stall de forma más realista (actualmente el modelo CL = CLα·α es lineal y no representa la pérdida; pendiente para cuando se trabaje con datos reales de perfiles NACA)
- [ ] Nivel 4: perfiles NACA (0012, 2412, 4412...) y comparación entre ellos
- [ ] Nivel 5: interfaz gráfica con Tkinter

## Tecnologías

- Python
- NumPy
- Matplotlib
- Tkinter (próximamente)

## Estructura del proyecto

\```
aircraft-aerodynamics/
├── main.py
├── aerodynamics.py
├── calculations.py
├── README.md
└── data/
\```

## Cómo ejecutarlo

\```bash
pip install numpy matplotlib
python main.py
\```
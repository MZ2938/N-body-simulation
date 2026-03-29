![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green)
![NumPy](https://img.shields.io/badge/NumPy-vectorized-orange)

# N-Body Simulation

Gravitational simulation of N particles in Python.

<div align="center">
  <img src="simulation.gif" alt="Demo nbody simulation" width="700"/>
</div>


## Run

```bash
pip install pygame numpy
python nbody.py
```

## Controls

| Key | Action |
|--------|--------|
| ← → ↑ ↓ | Move the view |
| Z / S | Zoom in / out |
| P | Screenshot |

## Physics

Each particle is affected by the gravitational force of all the others:

$$a_i = \sum_{j \neq i} G \cdot m_j \cdot \frac{r_j - r_i}{|r_j - r_i|^3}$$

Uses Euler integration.

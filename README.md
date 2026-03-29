![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green)
![NumPy](https://img.shields.io/badge/NumPy-vectorized-orange)

# N-Body Simulation

Simulation gravitationnelle de N particules en Python.

<div align="center">
  <img src="simulation.gif" alt="Demo nbody simulation" width="700"/>
</div>


## Lancer

```bash
pip install pygame numpy
python nbody.py
```

## Contrôles

| Touche | Action |
|--------|--------|
| ← → ↑ ↓ | Déplacer la vue |
| Z / S | Zoom avant / arrière |
| P | Screenshot |

## Physique

Chaque particule subit l'attraction gravitationnelle de toutes les autres :

$$a_i = \sum_{j \neq i} G \cdot m_j \cdot \frac{r_j - r_i}{|r_j - r_i|^3}$$

Intégration par la méthode d'Euler.

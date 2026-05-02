# Parametric Analysis of Stresses on Inclined Planes

This project performs a parametric analysis of normal and shear stresses acting on an inclined section of a prismatic bar, based on Example 1.10 from *Mechanics of Materials* by Russell C. Hibbeler (7th Edition).

## Context
The scenario involves a square cross-section bar ($40 \text{ mm} \times 40 \text{ mm}$) subjected to an axial load of $800 \text{ N}$. While the textbook provides a static example, this script extrapolates the data into a dynamic scenario where the section angle ($\theta$) varies from $0^\circ$ to $180^\circ$.

## Mathematical Model
The script calculates stresses based on the following equilibrium equations:
- **Normal Stress ($\sigma$):** $\sigma = \sigma_{max} \cdot \sin^2(\theta)$
- **Shear Stress ($\tau$):** $\tau = \sigma_{max} \cdot \sin(\theta) \cdot \cos(\theta)$

Where $\sigma_{max} = \frac{P}{A_0} = 500 \text{ kPa}$.

## Features
- **Vectorized Computation:** Uses `NumPy` for high-performance trigonometric calculations.
- **Professional Visualization:** Generates high-resolution (300 DPI) plots using `Matplotlib`.
- **Automatic Annotations:** Identifies and labels critical points (maximum and minimum stresses).
- **Clean Code Architecture:** Organized into functional blocks for easy maintenance and readability.

## Requirements
- Python 3.x
- NumPy
- Matplotlib

## How to Run
Execute the script in your Python environment:
```bash
python "ex1,10.py"
```

## Results
The script outputs two visualization files:
1. `normal_stress.png`: Shows that normal stress peaks at $\theta = 90^\circ$.
2. `shear_stress.png`: Demonstrates that maximum shear occurs at $45^\circ$ and $135^\circ$ planes.

---
*Developed for technical reporting and mechanical engineering analysis.*
# 📊 Parametric Stress Analysis - Inclined Sections

![Language](https://img.shields.io/badge/Language-Python-blue)
![Library](https://img.shields.io/badge/Library-NumPy-green)
![Library](https://img.shields.io/badge/Library-Matplotlib-orange)
![Category](https://img.shields.io/badge/Category-Solid%20Mechanics-lightgrey)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📄 Overview

This repository contains a script for the **parametric analysis of stresses** acting on an inclined section of a prismatic bar. The project is based on **Example 1.10** from Russell C. Hibbeler's book, *Mechanics of Materials* (7th ed.).

The study analyzes a square section bar ($40 \text{ mm} \times 40 \text{ mm}$) under an axial load of $800 \text{ N}$. The main goal was to extrapolate the static textbook example into a dynamic scenario, where the section angle ($\theta$) varies from $0^\circ$ to $180^\circ$, allowing the observation of the behavior of **Normal Stress ($\sigma$)** and **Shear Stress ($\tau$)** across the entire spectrum.

---

## 🧠 What is Parametric Analysis?

In the context of Solid Mechanics, a parametric analysis allows us to understand how internal forces change as a specific variable (in this case, the angle of the cut) is modified. 

### This project automates:
- **Numerical Discretization:** Dividing the angular range into 500 parts for smooth curve generation.
- **Coordinate Transformation:** Converting degrees to radians for trigonometric processing.
- **Stress Mapping:** Applying fundamental statics formulas to every point in the domain.

---

## 🚀 Key Skills Demonstrated

- **Mathematical Modeling:** Implementation of stress transformation equations:
  - $\sigma = \sigma_{\text{max}} \cdot \sin^2(\theta)$
  - $\tau = \sigma_{\text{max}} \cdot \sin(\theta) \cdot \cos(\theta)$
- **Data Visualization:** Using Matplotlib to create technical plots with annotations, arrows, and precise peak indicators.
- **Automation:** Eliminating manual calculation errors by using vectorized operations with NumPy.

---

## 🛠️ Technologies & Tools

| Category | Detail |
| :--- | :--- |
| **Language** | Python 3.x |
| **Numerical Library** | NumPy |
| **Plotting Library** | Matplotlib |
| **Format** | Script (.py) |
| **Methodology** | Analytical / Parametric |

---

## 💡 Concepts Covered

- **Normal Stress ($\sigma$):** Reaches its maximum value ($500 \text{ kPa}$) at $90^\circ$ (perpendicular section).
- **Shear Stress ($\tau$):** Reaches its maximum and minimum peaks ($250 \text{ kPa}$ and $-250 \text{ kPa}$) at $45^\circ$ and $135^\circ$ respectively.
- **Reference Area ($A_0$):** Calculation of initial stress based on $P/A$ where $A = 0.04 \times 0.04 \text{ m}^2$.

---

## 🎓 Course Information

| Detail | Value |
| :--- | :--- |
| **Course** | Mechanics of Materials (Resistência dos Materiais) |
| **Institution** | Pontifical Catholic University of Campinas (PUC-Campinas) |
| **Campus** | Campus I |
| **Program** | Computer Engineering |
| **Semester** | 1st Semester 2026 |

---

## 📬 Contact Me

<div align="center"> 
  <a href="https://www.linkedin.com/in/nunes-andrade" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>
  <a href="https://instagram.com/jp_nunes.andrade" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white"></a>
  <a href="mailto:jpnunesandrade26@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <a href="https://www.alura.com.br/indica-dev/jpnunesandrade26" target="_blank"><img src="https://img.shields.io/badge/Alura-0077B5?style=for-the-badge&logo=alura&logoColor=white"></a> 
</div>

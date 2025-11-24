# 📝 Project Statement: Projectile Trajectory Simulator

## 1. Problem Statement

Traditional methods of teaching introductory kinematics often rely solely on manual calculations, which can obscure the relationship between initial parameters (velocity, angle) and the resulting trajectory. The problem this project addresses is the need for a **simple, accessible computational tool** that allows beginner students to quickly simulate, analyze, and verify the path of a projectile without manual number-crunching. This simulation provides a foundational application of subject concepts in a technical, code-based context.

## 2. Scope of the Project

### In-Scope:
* Calculation of projectile kinematics (position, velocity components, time, range) using foundational physics formulas.
* Application of iterative techniques (the `while` loop) for generating the time-step simulation.
* Implementation of **three major functional modules** (Input, Calculation, Simulation) to ensure modular code structure.
* Implementation of **robust validation and error handling** for user input.

### Out-of-Scope:
* Modeling external forces such as aerodynamic drag (air resistance).
* Considering variable gravity or changes in altitude.
* Graphical plotting or visualization.

## 3. Target Users

* **Aerospace/Engineering Students:** Beginners seeking practical application of kinematics and programming.
* **Physics Students:** Individuals needing a tool to verify homework or laboratory results for basic projectile motion.
* **Educators:** Instructors needing a quick, reliable demonstration tool for basic trajectory principles.

## 4. High-Level Features

The system provides three core functional modules:
1.  **Input Handler:** Gathers initial velocity and launch angle with immediate validation and allows for repeated simulation runs.
2.  **Metric Calculator:** Computes and summarizes total Time of Flight, Range, and initial velocity components.
3.  **Trajectory Generator:** Simulates the path and reports $(t, x, y)$ coordinates along with the instantaneous **trajectory angle ($\gamma$)** in a structured table.

# 🚀 Projectile Trajectory Simulation

## 🎯 Overview

This project is a **command-line Python tool** used to simulate and analyze the flight path of a projectile. It applies basic physics equations to calculate how far and how high an object flies when launched at an angle, providing a simple, interactive way to test different scenarios.

## ✨ Project Features

The program performs the following functions:

1.  **Input & Validation:** Takes initial launch speed and angle from the user and checks that the values are correct.
2.  **Summary Calculation:** Calculates the total time the object is in the air and the maximum distance it travels (Range).
3.  **Trajectory Output:** Generates a detailed table showing the object's position (X, Y) and its angle of flight at regular time intervals.
4.  **Interactive Run:** Allows the user to run multiple simulations back-to-back without restarting the program.

## ⚙️ Non-Functional Requirements (NFRs)

The project meets the following non-functional requirements:

| Requirement | Description | Fulfillment in Project |
| :--- | :--- | :--- |
| **Usability** | The interface is simple, intuitive, and interactive. | **Interactive "Try Again" Loop** allows users to run multiple simulations quickly. Output is a formatted, clear table. |
| **Reliability** | The application must handle invalid data gracefully without crashing. | Input checks (`try...except`) ensure the program runs reliably even if the user enters non-numeric data. |
| **Maintainability** | The code must be easy to update and debug. | Achieved through a clear, **modular structure** using separate Python functions for each task. |
| **Performance** | The calculation and simulation must execute instantly. | Calculations are based on efficient closed-form equations, ensuring immediate results. |

## 🛠️ Technologies & Tools

* **Language:** Python 3.x
* **Libraries:** `math` (standard library for trigonometric functions)
* **Version Control:** Git & GitHub
* **Development Environment:** VS Code

## 🏃 Steps to Run

### Prerequisites
* Ensure **Python 3.x** is installed on your system.

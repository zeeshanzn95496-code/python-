# 🚦 Python Traffic Signal & Emergency System

A simple, interactive command-line traffic signal simulation written in Python. This project simulates a standard 4-way traffic light cycle with support for an emergency vehicle override (ambulance).

## ✨ Features

- **Normal Traffic Mode:** Cycles through each road (`North`, `East`, `South`, `West`), turning one road **GREEN** while keeping all others **RED** for a set duration.
- **Ambulance Emergency Mode:** Allows you to instantly override the cycle for a specific road when an ambulance is detected, prioritizing that direction for a shorter emergency duration.
- **Interactive Menu:** Easy-to-use text interface to control the simulation loop, switch modes, or exit safely.

---

## 🛠️ Prerequisites

Make sure you have **Python 3.x** installed on your system. No external libraries or pip packages are required since it uses Python's built-in `time` module.

---

## 🚀 How to Run

1. Clone or download this repository/script file.
2. Open your terminal or command prompt in the directory containing the script.
3. Run the script using Python:

```bash
python traffic_signal.py
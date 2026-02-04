# BatteryShield 🔋🛡️
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Xubuntu](https://img.shields.io/badge/Xubuntu-blue?style=for-the-badge&logo=xfce&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
A lightweight Linux background utility that monitors battery health and forces you to plug in your charger when energy levels are critical.

## 🚀 Features
- **Real-time Monitoring**: Tracks battery percentage, charging status, and battery health.
- **Aggressive Alert**: When the battery drops below 20% (and isn't charging), a full-screen "Red Alert" locks the screen until you plug it in.
- **Data Logging**: Saves your battery history and health stats to a JSON file.
- **Gamification**: Earn "points" by maintaining healthy charging habits.

## 🛠️ Requirements
This script is designed for **Linux** systems (tested on Xubuntu/Ubuntu). It reads battery data from `/sys/class/power_supply/`.

You need Python 3 and the following packages:
```bash
sudo apt update
sudo apt install python3-tk libcanberra-gtk-module

```

## 📦 Installation & Usage

1. **Clone the repository:**
```bash
git clone [https://github.com/YOUR_USERNAME/BatteryShield-Linux.git](https://github.com/YOUR_USERNAME/BatteryShield-Linux.git)
cd BatteryShield-Linux

```


2. **Run the script:**
```bash
python3 battery_shield.py

```



## ⚙️ Configuration

You can easily modify the script constants at the top of the file:

* `CRITICAL_THRESHOLD`: Set the percentage for the alert (default is 20%).
* `CHECK_INTERVAL`: Frequency of battery checks in seconds.
* `LOG_FILE`: Path to save your battery history.

## 📊 How it works

The script uses a full-screen **Tkinter** window with a "Stay-on-Top" attribute. It prevents closing the window until the system detects a "Charging" status, effectively forcing the user to find a power source.

---

*Disclaimer: This tool is intended for personal use to help extend battery lifespan through better charging habits.*

```

---

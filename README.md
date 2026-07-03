# NitroSensualEnhanced

![Python 3.12+](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/PyQt5-Framework-blue?logo=qt)
[![Windows](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat&logo=windows&logoColor=white)](https://github.com/bulatziyatdinov/NitroSensualEnhanced)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**NitroSensualEnhanced** is a Windows fan control and monitoring app for Acer Nitro 
laptops and similar systems, might even work for Predator series. It provides 
GUI for controlling CPU and GPU fan speeds, and displays real-time temperature.

Program works only on **Windows** platform due to abusing the NitroSense service 
and needs admin rights for registry modification to control fans.

It's a fork of [KRWCLASSIC/NitroSensual](https://github.com/KRWCLASSIC/NitroSensual) [KRWCLASSIC/NitroSensual](https://github.com/KRWCLASSIC/NitroSensual) where 
I added some new features, refactored and optimized the original code.

## Screenshots

![Screenshot 1](https://images2.imgbox.com/aa/3b/jbvLucfT_o.png)
![Screenshot 2](https://images2.imgbox.com/78/95/iv1ifR3q_o.png)

## Features

- CPU and GPU Fan Speeds Control
- Real-time CPU and GPU Temperatures Display
- Auto Mode for Temperature Ranges with Editor
- Clean and User-friendly Interface
- Tray Icon for Fan Speeds Control

## How It Works

- **Fan control**: NitroSensual writes to the NitroSense registry keys and communicates with the PredatorSense service to set fan speeds.

- **Laptop monitoring**: Uses PSsvc (PredatorSense Service) to read temperatures and fan speeds.

## Installation

A ready-to-use Windows compiled app is available in the [**Releases**](https://github.com/bulatziyatdinov/NitroSensualEnhanced/releases) tab.

Project works on Python 3.12+. Versions below are not tested.

1. Clone the repository:

```bash
git clone https://github.com/bulatziyatdinov/NitroSensualEnhanced
```

2. Move into directory:

```bash
cd NitroSensualEnhanced
```

3.1 For `uv` users:

```bash
cd src
uv run main.py
```

3.2 For pip users:

- Create virtual environment:

```bash
python -m venv .venv
```

- Activate virtual environment:

For Windows:

```bash
.venv/Scripts/activate
```

For Linux/macOS (*only for development because program works only on Windows*):

```bash
source .venv/bin/activate
```

- Install requirements:

```bash
pip install -r requirements.txt
```

- Run program:

```bash
cd src
python main.py
```

## Build

Run `build.bat` to build executable.


## Notes

- You must enable "Custom" mode in NitroSense for fan control to work.
- You must have PredatorSense service (PSsvc) running to use this app.
- If something breaks, due to how it's designed you can reset fan speeds in NitroSense by manually setting speed or switching to Auto.

## License

This project is licensed under the terms of the [**MIT License**](LICENSE).

The original project is unlicensed
[KRWCLASSIC/NitroSensual](https://github.com/KRWCLASSIC/NitroSensual).

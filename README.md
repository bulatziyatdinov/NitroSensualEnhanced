# NitroSensualEnhanced

![Python 3.12+](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/PyQt5-Framework-blue?logo=qt)
[![Windows](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat&logo=windows&logoColor=white)](https://github.com/bulatziyatdinov/NitroSensualEnhanced)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

It's a fork of [KRWCLASSIC/NitroSensual](https://github.com/KRWCLASSIC/NitroSensual) [KRWCLASSIC/NitroSensual](https://github.com/KRWCLASSIC/NitroSensual) where I added some features:

- Tray Icon for fan control
- Menu bar
- Some optimizations
- Refactored code

Program works only on **Windows** platform due to abusing the NitroSense service 
and needs admin rights for registry modification to control fans.

## About

**NitroSensual** is a Windows fan control and monitoring app for Acer Nitro laptops 
and similar systems, might even work for Predator series. It provides bloatless 
GUI for controlling CPU and GPU fan speeds, and displays real-time temperature readings 
using LibreHardwareMonitor.

## Screenshots

![Screenshot 1](https://images2.imgbox.com/68/1e/7YsNP9XN_o.png)

![Screenshot 2](https://images2.imgbox.com/8d/8d/R3rdT4ok_o.png)

## Features

- Control CPU and GPU fan speeds (requires NitroSense in Custom mode)
- View real-time CPU and GPU temperatures
- Auto mode for temperature ranges with editor
- Automatic admin privilege elevation for registry access
- Clean PyQt5 interface

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
uv run src/main.py
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
python src/main.py
```

## Build

Use `build.bat` for build exe.


## Notes

- You must enable "Custom" mode in NitroSense for fan control to work.
- You must have PredatorSense service (PSsvc) running to use this app.
- If something breaks, due to how it's designed you can reset fan speeds in NitroSense by manually setting speed or switching to Auto.

## License

This project is licensed under the terms of the [**MIT License**](LICENSE).

The original project is unlicensed
[KRWCLASSIC/NitroSensual](https://github.com/KRWCLASSIC/NitroSensual).

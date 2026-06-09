import json
import os
import struct
import sys
import winreg

import pywintypes
import win32file

# Variables from original code that are not used
#LHM_DLL_PATH = None

SYSTEM_HEALTH_INDEXES = {
   1: "CPU_Temperature",
   2: "CPU_Fan_Speed",
   6: "GPU_Fan_Speed",
   10: "GPU1_Temperature",
}



DEFAULT_CONFIG_FILENAME = "config.json"
DEFAULT_CONFIG = {
    "auto_fan_config": [
        {"min": 0, "max": 39, "speed": 0},
        {"min": 40, "max": 49, "speed": 20},
        {"min": 50, "max": 59, "speed": 35},
        {"min": 60, "max": 69, "speed": 50},
        {"min": 70, "max": 79, "speed": 70},
        {"min": 80, "max": 89, "speed": 85},
        {"min": 90, "max": 100, "speed": 100},
    ],
    "mode": "Custom",
    "custom_cpu": 50,
    "custom_gpu": 50,
}

AVAILABLE_FAN_TYPES = (
    'cpu',
    'gpu',
)


def get_app_dir() -> str:
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))


def load_config(filepath: str = DEFAULT_CONFIG_FILENAME):
    if not os.path.exists(filepath):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        for k, v in DEFAULT_CONFIG.items():
            if k not in data:
                data[k] = v
        return data
    except Exception:
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()


def save_config(config: dict, filepath: str = DEFAULT_CONFIG_FILENAME) -> None:
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=2)
    except Exception as e:
        print("Failed to save config:", e)


# Helper to read current fan percentage from registry
def read_fan_speed(fan_type: str) -> int:
    key_path = r"SOFTWARE\\OEM\\NitroSense\\FanControl"
    value_name = "CPUFanPercentage" if fan_type == "cpu" else "GPU1FanPercentage"
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0,
                            winreg.KEY_READ | winreg.KEY_WOW64_64KEY) as key:
            value, _ = winreg.QueryValueEx(key, value_name)
            return int(value)
    except Exception:
        return -1  # Could not read


# Helper to write fan percentage to registry
def write_fan_speed(fan_type: str, percent: int) -> None:
    key_path = r"SOFTWARE\\OEM\\NitroSense\\FanControl"
    value_name = "CPUFanPercentage" if fan_type == "cpu" else "GPU1FanPercentage"
    with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, key_path, 0,
                            winreg.KEY_SET_VALUE | winreg.KEY_WOW64_64KEY) as key:
        winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD, percent)


# Helper to apply fan speed via named pipe
def apply_fan_speed(fan_type: str, percent: int) -> None:
    fan_group_type = 1 if fan_type == "cpu" else 4
    data = (percent << 8) | fan_group_type
    packet = struct.pack("<HBIQ", 16, 1, 8, data)
    try:
        handle = win32file.CreateFile(
            r"\\.\pipe\PredatorSense_service_namedpipe",
            win32file.GENERIC_READ | win32file.GENERIC_WRITE,
            0,
            None,
            win32file.OPEN_EXISTING,
            0,
            None
        )
        win32file.WriteFile(handle, packet)
        resp = win32file.ReadFile(handle, 9)[1]
        win32file.CloseHandle(handle)
        return True, resp.hex()
    except Exception as e:
        return False, str(e)


def send_command_by_named_pipe(pipe, cmd_code: int, args: list) -> None:
    message = bytearray()
    message += struct.pack("<H", cmd_code)
    message += struct.pack("<B", len(args))
    for arg in args:
        message += struct.pack("<I", len(arg))
        message += arg
    win32file.WriteFile(pipe, message)
    win32file.FlushFileBuffers(pipe)


def decode_result(result):
    if result is None:
        return None
    if result & 0xFF == 0:
        return (result >> 8) & 0xFFFF
    return None


def get_acer_gaming_system_info(index: int, raw_result: bool = False) -> int | None:
    if index not in SYSTEM_HEALTH_INDEXES.keys():
        raise ValueError(
            f'{index} is invalid arg "index" value. Check utils.SYSTEM_HEALTH_INDEXES '
            'to look for valid options.'
        )
    input_code = 1 | (index << 8)
    arg = struct.pack("<I", input_code)
    try:
        pipe = win32file.CreateFile(
            r"\\.\pipe\PredatorSense_service_namedpipe",
            win32file.GENERIC_READ | win32file.GENERIC_WRITE,
            0, None, win32file.OPEN_EXISTING, 0, None
        )
        send_command_by_named_pipe(pipe, 13, [arg])
        _, raw = win32file.ReadFile(pipe, 13)
        result = struct.unpack_from("<Q", raw, 5)[0]
        win32file.CloseHandle(pipe)
        if raw_result:
            return result
        else:
            return decode_result(result)
    except (pywintypes.error, Exception):
        return None


def get_cpu_gpu_temp_and_rpm() -> tuple[int, int, int, int]:
    cpu_temp = get_acer_gaming_system_info(1)
    cpu_rpm = get_acer_gaming_system_info(2)
    gpu_temp = get_acer_gaming_system_info(10)
    gpu_rpm = get_acer_gaming_system_info(6)
    return cpu_temp, cpu_rpm, gpu_temp, gpu_rpm


# Functions from original code that are not used
# def unblock_file_if_needed(filepath):
#     # Unblock file if it has a zone identifier (Windows only)
#     if os.name == 'nt' and os.path.exists(filepath):
#         ads = filepath + ":Zone.Identifier"
#         if os.path.exists(ads):
#             try:
#                 os.remove(ads)
#             except Exception as e:
#                 print(f"Could not remove Zone.Identifier: {e}")

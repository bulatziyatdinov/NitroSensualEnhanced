APP_TITLE = 'NitroSensualEnhanced'
APP_VERSION = '1.1.0'
APP_TITLE_WITH_VERSION = APP_TITLE + ' ' + APP_VERSION

ICON_PATH = 'icon.png'

DEFAULT_CONFIG_FILENAME = 'config.json'

DEFAULT_CONFIG = {
    'auto_fan_config': [
        {'min': 0, 'max': 39, 'speed': 0},
        {'min': 40, 'max': 49, 'speed': 20},
        {'min': 50, 'max': 59, 'speed': 35},
        {'min': 60, 'max': 69, 'speed': 50},
        {'min': 70, 'max': 79, 'speed': 70},
        {'min': 80, 'max': 89, 'speed': 85},
        {'min': 90, 'max': 100, 'speed': 100},
    ],
    'mode': 'Custom',
    'custom_cpu': 50,
    'custom_gpu': 50,
    'tray_fan_custom_percent_values': [10, 20, 30, 50, 80],
}

SYSTEM_HEALTH_INDEXES = {
   1: 'CPU_Temperature',
   2: 'CPU_Fan_Speed',
   6: 'GPU_Fan_Speed',
   10: 'GPU1_Temperature',
}

# Variables from original code that are not used
# LHM_DLL_PATH = None

# AVAILABLE_FAN_TYPES = (
#     'cpu',
#     'gpu',
# )

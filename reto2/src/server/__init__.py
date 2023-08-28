import sys
import os
import configparser

# Añadir el directorio que contiene el paquete
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configuración inicial
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = configparser.ConfigParser()
config.read(os.path.join(base_dir, '.config'))

# Obtiene la ruta de ASSETS_DIR y la convierte en una ruta absoluta
ASSETS_DIR = os.path.join(base_dir, config['PATHS']['ASSETS_DIR'])

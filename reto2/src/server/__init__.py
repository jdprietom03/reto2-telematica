import sys
import os
import configparser

# Añadir el directorio que contiene el paquete
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configuración inicial
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '..', 'config', '.config'))

# Obtiene la ruta de ASSETS_DIR
ASSETS_DIR = config['PATHS']['ASSETS_DIR']

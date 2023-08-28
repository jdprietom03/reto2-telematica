import argparse
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde .env
load_dotenv()

# Configura el parser de argumentos
parser = argparse.ArgumentParser(
    description='Ejecuta componentes del proyecto. Puede ser el servidor, el servidor de retry o el gateway.')

parser.add_argument('mode',
                    type=str,
                    choices=['server', 'gateway'], 
                    help='Especifica el componente a ejecutar. "server" para correr el servidor y "gateway" para el gateway.')

args = parser.parse_args()

if args.mode == 'server':
    # Importa y ejecuta el código del servidor
    pass
elif args.mode == 'gateway':
    # Importa y ejecuta el código del gateway
    from api_gateway import gateway
    gateway.run()

from dotenv import load_dotenv
import os
from common.tools.logger import papertrail_logging

load_dotenv(verbose=True)

# Poner aquí cualquier otra variable que haya que cargar del archivo .env
# En el caso de Algorithmia en lugar de un .env se setea un Secret desde la aplicación web

APP_NAME = os.getenv('APP_NAME', 'MY_APP')

ENV_VAR = os.getenv('ENV_VAR')
STORAGE_LOGS = os.getenv('STORAGE_LOGS')

PAPERTRAIL_ADDRESS = os.getenv('PAPERTRAIL_ADDRESS')
PAPERTRAIL_UDP_PORT = os.getenv('PAPERTRAIL_UDP_PORT')

logger = papertrail_logging(address=(PAPERTRAIL_ADDRESS, int(PAPERTRAIL_UDP_PORT)), app_name=APP_NAME)

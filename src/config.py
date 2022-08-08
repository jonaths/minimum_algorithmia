from dotenv import load_dotenv
import os


load_dotenv(verbose=True)

# Poner aquí cualquier otra variable que haya que cargar del archivo .env

ENV_VAR = os.getenv('ENV_VAR')
STORAGE_LOGS = os.getenv('STORAGE_LOGS')

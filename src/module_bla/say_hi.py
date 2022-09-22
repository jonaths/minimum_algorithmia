import config
from config import logger


def hello(name: str):

    logger.info('This is an info log')
    logger.warning('This is a warning log')

    return f"hello {name}. Nice to meet you. There is an env variable {config.ENV_VAR}"

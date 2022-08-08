import config

def hello(name: str):
    return f"hello {name}. Nice to meet you. There is an env variable {config.ENV_VAR}"

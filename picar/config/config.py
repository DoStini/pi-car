from dotenv import dotenv_values

config = {}

def load_config():
    global config
    config = {
        **dotenv_values(".env"),
        **dotenv_values(".env.local"),
    }
    config["PORT"] = int(config["PORT"])
    config["FORWARD_PIN"] = int(config["FORWARD_PIN"])
    config["BACKWARDS_PIN"] = int(config["BACKWARDS_PIN"])
    config["RIGHT_PIN"] = int(config["RIGHT_PIN"])
    config["LEFT_PIN"] = int(config["LEFT_PIN"])

def get_config():
    global config
    if not config:
        load_config()

    return config

from dotenv import dotenv_values

def load_config():
    config = {
        **dotenv_values(".env"),
        **dotenv_values(".env.local"),
    }
    config["PORT"] = int(config["PORT"])
    return config

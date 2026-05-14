import os
from constants import CONFIG_FILE


def get_config_file():
    try:
        home_dir = os.environ["HOME"]
        return os.path.join(home_dir, CONFIG_FILE)
    except FileNotFoundError:
        print("Error: .mmcc_config.json was not found.")
    return None

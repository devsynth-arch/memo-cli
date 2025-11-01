
import os
import json

def get_storage_path():
    """Gets the path to the memo.json file."""
    home_dir = os.path.expanduser("~")
    return os.path.join(home_dir, ".memo.json")

def read_commands():
    """Reads the commands from the JSON file."""
    storage_path = get_storage_path()
    if not os.path.exists(storage_path):
        return {}
    with open(storage_path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def write_commands(commands):
    """Writes the commands to the JSON file."""
    storage_path = get_storage_path()
    with open(storage_path, "w") as f:
        json.dump(commands, f, indent=4)

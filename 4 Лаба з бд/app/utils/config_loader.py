import yaml
import os

def load_config(path):
    base = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base, "config", "app.yml")

    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

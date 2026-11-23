import os

def greet(name):
    env = os.environ["APP_ENV"]
    return f"Hello {name} from {env}"
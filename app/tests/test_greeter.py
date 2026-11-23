import os
from app.greeter import greet

def test_greet():
    assert greet("Rossi") == f"Hello Rossi from {os.environ['APP_ENV']}"
import pgzrun
import os
import sys

sys.path.append(os.getcwd())

from src.app import App
from src.input import InputHandler

WIDTH = 800
HEIGHT = 480
TITLE = "Cavern"

app = App()
input_handler = InputHandler()

def update():
    input_state = input_handler.get_state(keyboard)
    
    app.update(input_state)

def draw():
    screen.clear()
    app.draw()

pgzrun.go()
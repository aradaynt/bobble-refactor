from src.screens.menu import MenuScreen
from src.screens.play import PlayScreen
from src.screens.game_over import GameOverScreen

class App:
    def __init__(self):
        self.active_screen = MenuScreen(self)

    def update(self, input_state):
        if self.active_screen:
            self.active_screen.update(input_state)

    def draw(self):
        if self.active_screen:
            self.active_screen.draw()

    def switch_to_play(self):
        self.active_screen = PlayScreen(self)

    def switch_to_menu(self):
        self.active_screen = MenuScreen(self)
    
    def switch_to_game_over(self):
        self.active_screen = GameOverScreen(self)
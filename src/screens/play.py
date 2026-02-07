from src.game import Game
from src.input import InputState

class PlayScreen:
    def __init__(self, app):
        self.app = app
        from src.game import Player 
        self.game = Game(Player())

    def update(self, input_state: InputState):
        if input_state.pause_pressed:
            self.app.switch_to_pause()
            return
        
        if self.game.player.lives < 0:
            self.app.switch_to_game_over()
        else:
            self.game.update(input_state)

    def draw(self):
        self.game.draw()
from src.input import InputState

class GameOverScreen:
    def __init__(self, app):
        self.app = app
        self.final_game = app.active_screen.game if hasattr(app.active_screen, 'game') else None

    def update(self, input_state: InputState):
        if input_state.fire_pressed:
            self.app.switch_to_menu()

    def draw(self):
        if self.final_game:
            self.final_game.draw()
        
        screen.blit("over", (0, 0))
from src.input import InputState

class PauseScreen:
    def __init__(self, app, play_screen):
        self.app = app
        self.play_screen = play_screen

    def update(self, input_state: InputState):
        if input_state.pause_pressed:
            self.app.resume_play(self.play_screen)

    def draw(self, screen):
        self.play_screen.draw(screen)
        screen.draw.text("PAUSED", center=(400, 240), fontsize=60, color="white", owidth=1.5, ocolor="black")
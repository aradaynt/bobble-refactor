from src.input import InputState

class MenuScreen:
    def __init__(self, app):
        self.app = app
        self.timer = 0

    def update(self, input_state: InputState):
        self.timer += 1
        
        if input_state.fire_pressed:
            self.app.switch_to_play()

    def draw(self,screen):
        screen.blit("title", (0, 0))
        anim_frame = min(9, (self.timer // 4) % 160)
        screen.blit("space" + str(anim_frame), (0, 0))
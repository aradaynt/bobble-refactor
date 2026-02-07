from dataclasses import dataclass

@dataclass
class InputState:
    left: bool = False
    right: bool = False
    up: bool = False
    jump_pressed: bool = False
    fire_pressed: bool = False
    fire_held: bool = False
    pause_pressed: bool = False 

class InputHandler:
    def __init__(self):
        self.last_fire = False
        self.last_jump = False
        self.last_pause = False

    def get_state(self, keyboard) -> InputState:
        is_fire_down = keyboard.space
        is_jump_down = keyboard.up
        is_pause_down = keyboard.p 

        state = InputState(
            left=keyboard.left,
            right=keyboard.right,
            up=keyboard.up,
            jump_pressed=is_jump_down and not self.last_jump,
            fire_pressed=is_fire_down and not self.last_fire,
            fire_held=is_fire_down,
            pause_pressed=is_pause_down and not self.last_pause
        )

        self.last_fire = is_fire_down
        self.last_jump = is_jump_down
        self.last_pause = is_pause_down

        return state

class GameState:
    def __init__(self):
        self.previous_state = None

    def set_previous_state(self, state):
        self.previous_state = state

    def return_to_previous_state(self):
        return self.previous_state
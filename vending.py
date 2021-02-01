from buttons import Buttons
from lcd import Display


class Machine():
    def __init__(self):
        self.buttons = Buttons()
        self.display = Display()

    def buttons_light_on(self):
        self.buttons.turn_on_light()

    def buttons_light_off(self):
        self.buttons.turn_off_light()

    def display_test(self):
        self.display.main()
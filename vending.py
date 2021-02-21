from buttons import Buttons
from lcd import Display


class Machine:
    def __init__(self):
        # инициализация переменных
        self.any_button = False
        self.button_n = {}
        for k in range(1, 5):
            self.button_n.update({k: False})

        # инициализация устройств
        self.display = Display()
        self.buttons = Buttons(self)



    def buttons_light_on(self):
        self.buttons.turn_on_light()

    def buttons_light_off(self):
        self.buttons.turn_off_light()

    def rus_string(self):
        self.display.print_rus_string((((0, 4), 'Здравствуйте!'),
                                       ((2, 6), 'Нажмите'),
                                       ((3, 4), 'одну из кнопок')))


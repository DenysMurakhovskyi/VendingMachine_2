from buttons import Buttons
from lcd import Display
from temperature import Temp
import RPi.GPIO as GPIO


class Machine:
    def __init__(self):
        # инициализация переменных
        self.any_button = False
        self.button_n = {}
        for k in range(1, 5):
            self.button_n.update({k: False})

        # инициализация GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        # инициализация устройств
        self.display = Display()
        self.buttons = Buttons(self)
        self.t = Temp()

    def buttons_light_on(self):
        self.buttons.turn_on_light()

    def buttons_light_off(self):
        self.buttons.turn_off_light()

    def wait_any_key(self):
        self.buttons.wait_any_key()


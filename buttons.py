import pcf8574_io
import RPi.GPIO as GPIO
import configparser
import os
from time import sleep
import sys


class Buttons():
    def __init__(self, vm):
        GPIO.cleanup()
        self.state = False
        GPIO.setmode(GPIO.BCM)

        vm.display.print_rus_string((((1, 3), 'Инициализация'),
                                     ((2, 7), 'Кнопок')))

        sleep(0.75)
        vm.display.clear()

        try:
            if os.path.exists('config.cfg'):
                config = configparser.ConfigParser()
                config.read('config.cfg')
                self.buttons = {0: int(config.get("BUTTONS", 'int')),
                                1: config.get("BUTTONS", "button1"),
                                2: config.get("BUTTONS", "button2"),
                                3: config.get("BUTTONS", "button3"),
                                4: config.get("BUTTONS", 'back')}
                vm.display.print_rus_string((((1, 7), 'Кнопки'),
                                             ((2, 2), 'инициализированы')))
            else:
                vm.display.print_rus_string((((1, 7), 'Ошибка'),
                                             ((2, 3), 'инициализации')))
                sys.exit(1)
        except:
            vm.display.print_rus_string((((1, 7), 'Ошибка'),
                                         ((2, 3), 'инициализации')))
            sys.exit(1)
        sleep(0.75)
        vm.display.clear()

        vm.display.print_rus_string((((1, 7), 'Тест'),
                                     ((2, 5), 'Подсветки')))

        GPIO.setwarnings(False)

        self.relay_ch = 18
        try:
            GPIO.setup(self.relay_ch, GPIO.OUT)
        except:
            pass

        self.turn_on_light()

        sleep(1)

        self.turn_off_light()

        self.p1 = pcf8574_io.PCF(0x20)
        GPIO.setup(self.buttons[0], GPIO.IN)

        for k in range(1, 5):
            self.p1.pin_mode(self.buttons[k], 'INPUT')

        GPIO.add_event_detect(self.buttons[0], GPIO.FALLING, bouncetime=200, callback=self.PRESSED)

    def PRESSED(self, PIN):
        for k in range(1, 5):
            if not self.p1.digital_read(self.buttons[k]):
                print(self.buttons[k])

    def turn_on_light(self):
        if not self.state:
            try:
                GPIO.output(self.relay_ch, GPIO.LOW)
                self.state = True
                return True
            except:
                return False

    def turn_off_light(self):
        if self.state:
            try:
                GPIO.output(self.relay_ch, GPIO.HIGH)
                self.state = False
                return True
            except:
                return False


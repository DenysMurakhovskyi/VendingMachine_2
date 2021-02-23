import pcf8574_io
import RPi.GPIO as GPIO
import configparser
import os
from time import sleep
import sys


class Buttons:
    def __init__(self, vm):
        self.parent = vm
        self.state = [False] * 4
        self.light_state = False
        self.anykey = False
        self.relay_ch = 18
        self.p1 = pcf8574_io.PCF(0x20)
        self.tested = [False] * 4
        self.testmode = False
        self.anykeymode = False

        self.parent.display.print_rus_string((((1, 3), 'Инициализация'),
                                     ((2, 7), 'Кнопок')))

        sleep(0.75)
        self.parent.display.clear()

        try:
            if os.path.exists('config.cfg'):
                config = configparser.ConfigParser()
                config.read('config.cfg')
                self.buttons = {0: int(config.get("BUTTONS", 'int')),
                                1: config.get("BUTTONS", "button1"),
                                2: config.get("BUTTONS", "button2"),
                                3: config.get("BUTTONS", "button3"),
                                4: config.get("BUTTONS", 'back')}
                GPIO.setup(self.buttons[0], GPIO.IN)
                for k in range(1, 5):
                    self.p1.pin_mode(self.buttons[k], 'INPUT')

                self.parent.display.print_rus_string((((1, 7), 'Кнопки'),
                                             ((2, 2), 'инициализированы')))
            else:
                self.parent.display.print_rus_string((((1, 7), 'Ошибка'),
                                             ((2, 3), 'инициализации')))
                sys.exit(1)
        except:
            self.parent.display.print_rus_string((((1, 7), 'Ошибка'),
                                         ((2, 3), 'инициализации')))
            sys.exit(1)
        sleep(0.75)
        self.parent.display.clear()

        self.parent.display.print_rus_string((((1, 8), 'Тест'),
                                     ((2, 5), 'Подсветки')))

        try:
            GPIO.setup(self.relay_ch, GPIO.OUT)
        except:
            pass

        self.turn_on_light()
        sleep(1)
        self.turn_off_light()
        self.parent.display.clear()

        GPIO.add_event_detect(self.buttons[0], GPIO.FALLING, bouncetime=200, callback=self.PRESSED)

    def PRESSED(self, PIN):
        if self.anykeymode:
            self.anykey = True
        for k in range(1, 5):
            if not self.p1.digital_read(self.buttons[k]):
                if self.testmode:
                    self.tested[k - 1] = True
                    self.parent.display.clear()
                    self.parent.display.print_rus_string((((1, 7), 'Нажата'),
                                                          ((2, 5), 'кнопка #{:d}'.format(k))))
                else:
                    pass

    def run_key_test(self):
        self.testmode = True
        self.parent.display.clear()
        self.parent.display.print_rus_string((((1, 4), 'Тестирование'),
                                              ((2, 6), 'нажатий')))

        while self.tested != [True] * 4:
            pass
        self.turn_on_light()
        sleep(0.5)
        self.turn_off_light()
        self.parent.display.clear()
        self.parent.display.print_rus_string((((1, 8), 'Тест'),
                                              ((2, 3), 'кнопок окончен')))
        self.testmode = False

    def wait_any_key(self):
        self.anykeymode = True
        while not self.anykey:
            pass
        self.anykey = False
        self.parent.display.clear()

    def turn_on_light(self):
        if not self.light_state:
            try:
                GPIO.output(self.relay_ch, GPIO.LOW)
                self.light_state = True
                return True
            except:
                return False

    def turn_off_light(self):
        if self.light_state:
            try:
                GPIO.output(self.relay_ch, GPIO.HIGH)
                self.light_state = False
                return True
            except:
                return False


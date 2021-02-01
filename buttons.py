import RPi.GPIO as GPIO
import time

pins = {1: 6, 2: 5, 3: 16, 4: 26}
relay_ch = 23


class Buttons():
    def __init__(self):
        self.state = False
        GPIO.setmode(GPIO.BCM)

        for item in pins.values():
            GPIO.setup(item, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.setwarnings(False)
        try:
            GPIO.setup(relay_ch, GPIO.OUT)
        except:
            pass

    def turn_on_light(self):
        if not self.state:
            try:
                GPIO.output(relay_ch, GPIO.LOW)
                self.state = True
                return True
            except:
                return False

    def turn_off_light(self):
        if self.state:
            try:
                GPIO.output(relay_ch, GPIO.HIGH)
                self.state = False
                return True
            except:
                return False

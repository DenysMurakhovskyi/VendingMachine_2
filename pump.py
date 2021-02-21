import RPi.GPIO as GPIO
import time

value = 0

pin = 23

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)


def PRESSED(PIN):
    global value
    value += 1
    print('Detected!', value)


GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.RISING, bouncetime=10, callback=PRESSED)

while True:
    pass

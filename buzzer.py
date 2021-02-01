import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
BUZZER= 22
buzzState = True
GPIO.setup(BUZZER, GPIO.OUT)

for i in range(0, 5):
    buzzState = not buzzState
    GPIO.output(BUZZER, buzzState)
    time.sleep(0.1)
    buzzState = not buzzState
    GPIO.output(BUZZER, buzzState)
    time.sleep(0.7)
    
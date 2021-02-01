import RPi.GPIO as GPIO
import time

pins = {1: 6, 2: 5, 3: 16, 4: 26}
GPIO.setmode(GPIO.BCM)

for item in pins.values():
    GPIO.setup(item, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def detect_press():
    while True:
        input_state = [GPIO.input(pin) for pin in pins.values()]
        if not input_state[0]:
            print('Button 1 pressed')
            # b.pressed_button = 0
        elif not input_state[1]:
            print('Button 2 pressed')
            # b.pressed_button = 1
        elif not input_state[2]:
            print('Button 3 pressed')
            # b.pressed_button = 2
        elif not input_state[3]:
            print('Button 4 pressed')
            # b.pressed_button = 3
        time.sleep(0.3)


if __name__ == '__main__':
    detect_press()
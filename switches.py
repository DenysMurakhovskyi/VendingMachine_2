import pcf8574_io
import RPi.GPIO as GPIO

p1 = pcf8574_io.PCF(0x25)
GPIO.setmode(GPIO.BCM)
pin = 20

p1.pin_mode('p2', 'INPUT')
p1.pin_mode('p4', 'INPUT')
p1.pin_mode('p5', 'INPUT')
p1.pin_mode('p7', 'INPUT')


def PRESSED(PIN):
    if not p1.digital_read('p2'):
        print('1-on')
    elif p1.digital_read('p2'):
        print('1-off')
    if not p1.digital_read('p4'):
        print('2-on')
    elif p1.digital_read('p4'):
        print('2-off')


GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.FALLING, bouncetime=200, callback=PRESSED)

while True:
    pass
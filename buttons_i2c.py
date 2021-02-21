import pcf8574_io
import RPi.GPIO as GPIO

p1 = pcf8574_io.PCF(0x20)
GPIO.setmode(GPIO.BCM)
pin = 19

p1.pin_mode('p4', 'INPUT')
p1.pin_mode('p5', 'INPUT')
p1.pin_mode('p6', 'INPUT')
p1.pin_mode('p7', 'INPUT')


def PRESSED(PIN):
    if not p1.digital_read('p4'):
        print('P4')
    if not p1.digital_read('p5'):
        print('P5')
    if not p1.digital_read('p6'):
        print('P6')
    if not p1.digital_read('p7'):
        print('P7')


GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.FALLING, bouncetime=200, callback=PRESSED)

while True:
    pass
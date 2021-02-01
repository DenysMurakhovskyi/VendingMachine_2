import adafruit_dht as ad
import board
import RPi.GPIO as GPIO
import time

try:
    # dht_11 = ad.DHT11(board.D23, False)
    dht_22 = ad.DHT22(board.D4, False)
except:
    # dht_11.exit()
    dht_22.exit()

temperature = dht_22.temperature
if temperature is not None:
    print("Temp={0:0.1f}*C".format(temperature))
else:
    print("Failed to retrieve data from DHT11 sensor")
dht_22.exit()

    
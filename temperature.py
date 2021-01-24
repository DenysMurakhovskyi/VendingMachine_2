import adafruit_dht as ad
import board
import RPi.GPIO as GPIO

try:
    dht_device = ad.DHT22(board.D12, False)
except:
    dht_device.exit()

humidity, temperature = dht_device.humidity, dht_device.temperature
if humidity is not None and temperature is not None:
    print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
else:
    print("Failed to retrieve data from humidity sensor")
dht_device.exit()

    
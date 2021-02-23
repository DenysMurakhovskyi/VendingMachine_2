import adafruit_dht as ad
import board
import RPi.GPIO as GPIO
import time


class Temp:
    def __init__(self):
        try:
            self.dht_1 = ad.DHT22(board.D4, False)
            self.dht_2 = ad.DHT22(board.D27, False)
        except:
            self.dht_1.exit()
            self.dht_2.exit()
            raise IOError

    def get_temperature(self):
        return {1: self.dht_1.temperature, 2: self.dht_2.temperature}

    def get_humidity(self):
        return {1: self.dht_1.humidity, 2: self.dht_2.humidity}
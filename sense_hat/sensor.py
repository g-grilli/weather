#!usr/bin/env python 3
from sense_hat import SenseHat

sense = SenseHat() 
temp = sense.get_temperature()
humidity = sense.get_humidity()
pressure = sense.get_pressure()

def temperature(temp):
  return round((temp / 5 * 9) + 32, 1)
  
def bar(pressure):
  return round((pressure / 0.02952998751, 1))

def hum(humidity):
  return round(humidity)

print("Temperature: %s C" % temp)
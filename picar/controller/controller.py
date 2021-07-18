import RPi.GPIO as gpio
from time import sleep

from picar.config import config

cfg = config.get_config()

print(cfg)

PINS = [
    cfg["FORWARD_PIN"],
    cfg["BACKWARDS_PIN"],
    cfg["RIGHT_PIN"],
    cfg["LEFT_PIN"],
]


def pin_on(pin):
    gpio.output(pin, 1)

def pin_off(pin):
    gpio.output(pin, 0)

def setup():
    gpio.setmode(gpio.BCM)
    for pin in PINS:
        gpio.setup(PINS, gpio.OUT)

setup()

for x in range(2):
    for pin in PINS:
        pin_on(pin)
    sleep(1)
    for pin in PINS:
        pin_off(pin) 
    sleep(1)

gpio.cleanup()

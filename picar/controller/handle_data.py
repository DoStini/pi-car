from gpiozero import LED
from time import sleep
led = LED(21)

while True:
    led.toggle()
    sleep(1)

def toggle():
    led.toggle()
    print(led.value)

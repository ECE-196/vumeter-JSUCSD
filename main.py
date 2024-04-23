import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, #type:ignore
    board.IO47,
    board.IO33, #type:ignore
    board.IO34, #type:ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
]

leds = [DigitalInOut(pin) for pin in led_pins]

thresholds = [20000, 25000, 26000, 27000, 28000, 30000, 40000, 45000, 50000, 51000, 52000]

for led in leds:
    led.direction = Direction.OUTPUT

while True:
    volume = microphone.value

    print(volume)

    leds_to_light = 0
    for i, threshold in enumerate(thresholds):
        if volume >= threshold:  # Check if volume exceeds the threshold
            leds_to_light = i + 1  

    # Turn on/off LEDs
    for i, led in enumerate(leds):
        led.value = i < leds_to_light

    sleep(0.1)

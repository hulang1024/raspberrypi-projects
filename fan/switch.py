import RPi.GPIO as GPIO
import time

class Switch:
    def __init__(self, pin):
        self.pin = pin
        self._is_on = False
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(pin, GPIO.OUT)

    def __del__(self):
        self.turn_off()
        GPIO.cleanup()

    def turn_off(self):
        GPIO.output(self.pin, 1)
        self._is_on = False

    def turn_on(self):
        GPIO.output(self.pin, 0)
        self._is_on = True

    def is_on(self):
        return self._is_on

if __name__ == '__main__':
    switch = Switch(31)
    time.sleep(2)
    switch.turn_on()

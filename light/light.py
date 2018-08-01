import RPi.GPIO as GPIO
import time
import math

class Light:
    def __init__(self, pin):
        self.__pin = pin
        self.__pwm = None
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    def __del__(self):
        print(self.__class__.__name__, 'del')
        self.brightness_turn_off()
        self.turn_off()

    def turn_on(self):
        GPIO.output(self.__pin, GPIO.HIGH)

    def turn_off(self):
        self.brightness_turn_off()
        GPIO.output(self.__pin, GPIO.LOW)

    def brightness_turn_on(self, value):
        if self.__pwm == None:
            self.__pwm = GPIO.PWM(self.__pin, 4000)
            self.__pwm.start(0)
        dc = math.floor(value / 255.0 * 100)
        self.__pwm.ChangeDutyCycle(dc)

    def brightness_turn_off(self):
        if self.__pwm != None:
            self.__pwm.stop()
            self.__pwm = None

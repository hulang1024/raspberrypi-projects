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

if __name__ == '__main__':
    r_light = Light(11)
    g_light = Light(12)
    b_light = Light(13)

    f = True
    v = 10
    while True:
        #r = int(input('r='))
        #g = int(input('g='))
        #b = int(input('b='))
        v = 100 if f else 255
        r = g = b = v
        f = not f
        r_light.brightness_turn_on(r)
        g_light.brightness_turn_on(g)
        b_light.brightness_turn_on(b)
        time.sleep(1)

    time.sleep(10)

    try:
        pass
    finally:
        print('cleanup')
        GPIO.cleanup()

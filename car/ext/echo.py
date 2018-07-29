
import time
import RPi.GPIO as GPIO

class DistanceGetter:
    def __init__(self, trig_pin, echo_pin):
        self.__trig_pin = trig_pin
        self.__echo_pin = echo_pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(trig_pin, GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(echo_pin, GPIO.IN)

    def get_distance(self):
        GPIO.output(self.__trig_pin, GPIO.HIGH)
        time.sleep(0.000015)
        GPIO.output(self.__trig_pin, GPIO.LOW)

        start_time = time.time()
        while not GPIO.input(self.__echo_pin):
            pass
        while GPIO.input(self.__echo_pin):
            pass
        #计算秒级时差
        echo_secs = time.time() - start_time
        #根据音速340/s计算距离
        metres = echo_secs * 340 / 2

        return metres


if __name__ == '__main__':
    d = DistanceGetter(11, 12)

    try:
        while True:
            print('%.2fm' % d.get_distance())
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()

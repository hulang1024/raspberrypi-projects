# -*- coding: utf-8 -*-

import time
import threading
import RPi.GPIO as GPIO
from car import Car

class DistanceSensor(threading.Thread):
    def __init__(self, trig_pin, echo_pin):
        threading.Thread.__init__(self)

        self.__trig_pin = trig_pin
        self.__echo_pin = echo_pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(trig_pin, GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(echo_pin, GPIO.IN)

        self.__flag = threading.Event() #用于暂停线程的标识
        self.__flag.set()
        self.__running = threading.Event()
        self.__running.set()

        self.last_distance = 0

    def init(self):
        self.setDaemon(True)
        self.start()

    def connect(self, car):
        self.car = car

    def on_car_run(self):
        self.resume()

    def on_car_stop(self):
        self.pause()

    def on_exit(self):
        self.stop()

    def run(self):
        while self.__running.isSet():
            self.__flag.wait()
            distance = self.get_distance()
            if abs(distance - self.last_distance) > 0.1:
                self.last_distance = distance
                self.car.on_distance_change(distance)
            time.sleep(0.01)

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

    def pause(self):
        self.__flag.clear()

    def resume(self):
        self.__flag.set()

    def stop(self):
        self.__flag.set()
        self.__running.clear()

# -*- coding: utf-8 -*-

"""
    小车
"""

import time
import RPi.GPIO as GPIO
import motor_driver

class Car:
    DIR_FORE = 1
    DIR_BACK = 2

    def __init__(self, motor_driver, distance_sensor):
        """
        构造一个单电机驱动器小车控制器
        :param motor_driver 电机驱动，M1电机用作左侧轮，M2电机用作右侧轮
        :param extends 扩展模块数组
        """
        self.__motor_driver = motor_driver
        self.__distance_sensor = distance_sensor
        self.__speed = 13
        self.__started = False
        self.__dir = Car.DIR_FORE
        self.extends = []
        self.connect_extend(distance_sensor)

    def connect_extend(self, extend):
        self.extends.append(extend)
        extend.connect(self)
        extend.init()

    def dir(self):
        return self.__dir

    def speed(self):
        return self.__speed

    def is_runing(self):
        return self.__started

    def is_block(self):
        return self._is_block_distance(self.__distance_sensor.get_distance())

    def fore(self):
        """
        前进
        """
        self.__motor_driver.forward(1)
        self.__motor_driver.forward(2)
        self.__dir = Car.DIR_FORE
        self._start()

    def back(self):
        """
        后退
        """
        self.__motor_driver.reverse(1)
        self.__motor_driver.reverse(2)
        self.__dir = Car.DIR_BACK
        self._start()

    def turn_left(self):
        #self.__motor_driver.stop(1)
        self.__motor_driver.reverse(1)
        self.__motor_driver.forward(2)
        self.__dir = Car.DIR_FORE
        self._start()

    def turn_right(self):
        #self.__motor_driver.stop(2)
        self.__motor_driver.reverse(2)
        self.__motor_driver.forward(1)
        self.__dir = Car.DIR_FORE
        self._start()

    def change_speed(self, value):
        self.__motor_driver.change_speed(1, value)
        self.__motor_driver.change_speed(2, value)
        self.__speed = value

    def stop(self):
        """
        停止
        """
        self.__motor_driver.stop(1)
        self.__motor_driver.stop(2)
        self.__started = False
        for ext in self.extends:
            ext.on_car_stop()

    def on_exit(self):
        self.stop()
        for ext in self.extends:
            ext.on_exit()
        time.sleep(0.1)
        GPIO.cleanup()

    def _start(self):
        if not self.__started:
            self.__motor_driver.change_speed(1, self.__speed)
            self.__motor_driver.change_speed(2, self.__speed)
            self.__started = True
            for ext in self.extends:
                ext.on_car_run()

    def _is_block_distance(self, distance):
        return distance < 0.4

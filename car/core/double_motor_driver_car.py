# -*- coding: utf-8 -*-

"""
    双电机驱动器小车控制器
"""

import time
from core.car import Car
import core.motor_driver

class DoubleMotorDriverCar(Car):
    def __init__(self, motor_driver1, motor_driver2):
        """
        构造一个双电机驱动器小车控制器
        :param motor_driver1 前轮电机驱动，M1电机用作前左轮，M2电机用作前右轮
        :param motor_driver2 后轮电机驱动，M1电机用作后左轮，M2电机用作后右轮
        """
        self.__fron_motor_driver = motor_driver1
        self.__back_motor_driver = motor_driver2
        self.__lastCtrl = None

    def fore(self):
        """
        前进
        """
        if self.__lastCtrl == 'fore':
            return
        elif self.__lastCtrl == 'back':
            self.stop()
            time.sleep(0.1)

        self.__fron_motor_driver.forward(1)
        self.__fron_motor_driver.forward(2)
        self.__back_motor_driver.forward(1)
        self.__back_motor_driver.forward(2)
        self.__lastCtrl = 'fore'

    def back(self):
        """
        后退
        """
        if self.__lastCtrl == 'back':
            return
        elif self.__lastCtrl == 'fore':
            self.stop()
            time.sleep(0.1)

        self.__fron_motor_driver.reverse(1)
        self.__fron_motor_driver.reverse(2)
        self.__back_motor_driver.reverse(1)
        self.__back_motor_driver.reverse(2)
        self.__lastCtrl = 'back'

    def turn_left(self):
        self.__fron_motor_driver.stop(1)
        self.__back_motor_driver.stop(1)
        self.__fron_motor_driver.forward(2)
        self.__back_motor_driver.forward(2)
        self.__lastCtrl = 'turn_left'

    def turn_right(self):
        self.__fron_motor_driver.stop(2)
        self.__back_motor_driver.stop(2)
        self.__fron_motor_driver.forward(1)
        self.__back_motor_driver.forward(1)
        self.__lastCtrl = 'turn_right'

    def stop(self):
        """
        停止
        """
        self.__fron_motor_driver.stop(1)
        self.__fron_motor_driver.stop(2)
        self.__back_motor_driver.stop(1)
        self.__back_motor_driver.stop(2)
        self.__lastCtrl = 'stop'

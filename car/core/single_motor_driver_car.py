# -*- coding: utf-8 -*-

"""
    单电机驱动器小车控制器
"""

import time
from core.car import Car
import core.motor_driver

class SingleMotorDriverCar(Car):
    def __init__(self, motor_driver):
        """
        构造一个单电机驱动器小车控制器
        :param motor_driver 电机驱动，M1电机用作左侧轮，M2电机用作右侧轮
        """
        self.__motor_driver = motor_driver
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

        self.__motor_driver.forward(1)
        self.__motor_driver.forward(2)
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

        self.__motor_driver.reverse(1)
        self.__motor_driver.reverse(2)
        self.__lastCtrl = 'back'

    def turn_left(self):
        pass

    def turn_right(self):
        pass

    def stop(self):
        """
        停止
        """
        self.__motor_driver.stop(1)
        self.__motor_driver.stop(2)
        self.__lastCtrl = 'stop'

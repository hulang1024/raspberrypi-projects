# -*- coding: utf-8 -*-

import config
from car import *
from motor_driver import *
import echo

def new():
    car = Car(
        MotorDriver(
            config.motor_driver['in_pins'],
            config.motor_driver['enable_pins'][0],
            config.motor_driver['enable_pins'][1]),
        echo.DistanceSensor(31, 33))

    return car

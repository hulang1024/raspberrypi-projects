# -*- coding: utf-8 -*-

"""
    抽象小车控制器
"""

import RPi.GPIO as GPIO

class Car:
    def fore(self):
        pass

    def back(self):
        pass

    def turn_left(self):
        pass

    def turn_right(self):
        pass

    def stop(self):
        pass

    def on_exit(self):
        self.stop()
        GPIO.cleanup()

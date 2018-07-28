# -*- coding: utf-8 -*-

"""
    电机驱动器（带两个电机的）
"""

import RPi.GPIO as GPIO

class MotorDriver:
    __MOTOR_CTRL_OUT_TABLE = (
        ((1, 0, None, None),
         (0, 1, None, None),
         (0, 0, None, None)),
        ((None, None, 1, 0),
         (None, None, 0, 1),
         (None, None, 0, 0)))

    def __init__(self, in_pins):
        """
        创建一个电机驱动器
        :param in_pins 连接电机驱动IN口的BOARD模式编号的引脚编号，顺序1到4
        """
        self.__in_pins = in_pins

        GPIO.setmode(GPIO.BOARD)
        for p in in_pins:
            GPIO.setup(p, GPIO.OUT, initial=GPIO.LOW)

    def forward(self, motor_num):
        """
        正转电机
        :param motor_num 电机号 1或2
        """
        self._action(motor_num, 0)

    def reverse(self, motor_num):
        """
        反转电机
        :param motor_num 电机号 1或2
        """
        self._action(motor_num, 1)

    def stop(self, motor_num):
        """
        停转电机
        :param motor_num 电机号 1或2
        """
        self._action(motor_num, 2)

    def _action(self, motor_num, act):
        for i in range(0, 4):
            v = MotorDriver.__MOTOR_CTRL_OUT_TABLE[motor_num - 1][act][i]
            if v != None:
                GPIO.output(self.__in_pins[i], v)

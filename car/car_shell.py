# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import sys
import tty, termios
import config
from core.motor_driver import *
from core.double_motor_driver_car import *
from core.single_motor_driver_car import *


car = None
if config.motor_driver_count == 2:
    car = DoubleMotorDriverCar(
        MotorDriver(config.motor_driver_in_pins[0]),
        MotorDriver(config.motor_driver_in_pins[1]))
elif config.motor_driver_count == 1:
    car = SingleMotorDriverCar(
        MotorDriver(config.motor_driver_in_pins[0]))

if car == None:
    print('配置错误')
    exit()

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

print("""
操作说明:
  方向: W/S/A/D
  停止: Q
  退出: Ctrl+C
""")
while True:
    try:
        tty.setraw(fd)
        keysym = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    if keysym == 'w':
        print('前进')
        car.fore()
    elif keysym == 's':
        print('后退')
        car.back()
    elif keysym == 'a':
        print('左转')
        car.turn_left()
    elif keysym == 'd':
        print('右转')
        car.turn_right()
    elif keysym == 'q':
        print('停止')
        car.stop()
    elif ord(keysym) == 0x3: #ctrl c
        print('退出')
        break

car.stop()
GPIO.cleanup()

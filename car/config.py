# -*- coding: utf-8 -*-

"""
    配置小车硬件信息，如需知道更多信息请阅读代码
"""

#树莓派连接电机驱动器信息
motor_driver = {
    #IN口(IN1~IN4)的BOARD模式的引脚编号
    'in_pins': (11, 12, 13, 15),
    #使能口的BOARD模式的引脚编号:电机1,电机2
    'enable_pins': (35, 37)
}

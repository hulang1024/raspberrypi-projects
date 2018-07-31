# -*- coding: utf-8 -*-

"""
    配置小车硬件信息，如需知道更多信息请阅读代码
"""

#用了几个电机驱动器,可用值: 1,2
motor_driver_count = 1
#树莓派连接电机驱动IN口的BOARD模式编号的引脚编号,IN1~IN4
motor_driver_in_pins = (
    #第1个电机驱动器的
    (29, 31, 33, 35),
)

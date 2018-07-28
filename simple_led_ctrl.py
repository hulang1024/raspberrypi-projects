# -*- coding: utf-8 -*-

"""
    简单LED控制
"""

import RPi.GPIO as GPIO
from time import sleep
import sys
import tty, termios

#setup
output_nums = (11, 12, 37)
lamp_states = [False, False, False]
GPIO.setmode(GPIO.BOARD)
for num in output_nums:
    GPIO.setup(num, GPIO.OUT)

curr_index = 2 #当前灯索引
prev_index = 0 #上个灯索引

#关某个灯
def off_lamp(i):
    print('关%d号灯' % (i + 1))
    if not lamp_states[i]:
        return
    set_lamp(i, False)

#开某个灯
def on_lamp(i):
    print('开%d号灯' % (i + 1))
    if lamp_states[i]:
        return
    set_lamp(i, True)

def set_lamp(i, state):
    GPIO.output(output_nums[i], state)
    lamp_states[i] = state

#开关灯
def turn_lamp(i):
    if lamp_states[i]:
        off_lamp(i)
    else:
        on_lamp(i)

def off_all_lamps():
    set_all_lamps(False)

def on_all_lamps():
    set_all_lamps(True)

def set_all_lamps(state):
    print('%s所有灯' % ('开' if state else '关'))
    for i in range(0, len(output_nums)):
        set_lamp(i, state)

def flow_next():
    global prev_index, curr_index
    prev_index = curr_index
    curr_index += 1
    curr_index %= len(output_nums)
    off_lamp(prev_index)
    on_lamp(curr_index)

def flow_prev():
    global prev_index, curr_index
    prev_index = curr_index
    if curr_index > 0:
        curr_index -= 1
    else:
        curr_index = len(output_nums) - 1
    off_lamp(prev_index)
    on_lamp(curr_index)

#流水灯
def run_flow():
    loop_count = 6 #循环次数
    cnt = 0
    while cnt < loop_count:
        flow_next()
        cnt += 1
    off_all_lamps()

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
while True:
    try:
        tty.setraw(fd)
        keysym = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    if keysym.isdigit():
        n = int(keysym)
        if 1 <= n <= 3:
            turn_lamp(n - 1)
    elif keysym == 'q':
        off_all_lamps()
    elif keysym == 'e':
        on_all_lamps()
    elif keysym == 'd':
        flow_next()
    elif keysym == 'a':
        flow_prev()
    elif keysym == 'f':
        run_flow()
    elif ord(keysym) == 0x3: #ctrl c
        break
GPIO.clearnup()

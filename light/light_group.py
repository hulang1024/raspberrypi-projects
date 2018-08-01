import time
from light import *

r_light = Light(11)
g_light = Light(12)
b_light = Light(13)

__light_group = (r_light, g_light, b_light)

light_count = len(__light_group)

def turn_on(light_no):
    __light_group[light_no - 1].turn_on()

def turn_off(light_no):
    __light_group[light_no - 1].turn_off()

def brightness(light_no, value):
    __light_group[light_no - 1].brightness_turn_on(value)

def on_exit():
    pass

# -*- coding: utf-8 -*-

import time
import car_factory
import time


try:
    car = car_factory.new()
    print('go')
    while True:
        print('loop')
        if car.is_block():
            while car.is_block():
                print('back')
                car.back()
                time.sleep(0.1)
            print('turn_right')
            car.turn_right()
            time.sleep(2)
        else:
            car.fore()

except KeyboardInterrupt:
    car.stop()
    car.on_exit()

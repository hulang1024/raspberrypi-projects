# -*- coding: utf-8 -*-

"""
    websocket服务器
"""

import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
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

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        loader = tornado.template.Loader(".")
        self.write(loader.load("../car_web_ui/index.html").generate())

class WSHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True
    def open(self):
        print('connection opened...')
        self.write_message("The server says: 'Hello'. Connection was accepted.")

    def on_message(self, message):
        print('received:', message)
        code = message
        if code == 'fore':
            car.fore()
        elif code == 'back':
            car.back()
        elif code == 'turnLeft':
            car.turn_left()
        elif code == 'turnRight':
            car.turn_right()
        elif code == 'stop':
            car.stop()
        self.write_message("1")

    def on_close(self):
        print('connection closed...')

application = tornado.web.Application([
    (r'/ws', WSHandler),
    (r'/', IndexHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": "../car_web_ui"}),
])

if __name__ == "__main__":
    try:
        application.listen(9000)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        car.on_exit()

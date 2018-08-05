# -*- coding: utf-8 -*-

"""
    websocket服务器
"""

import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import json
import car_factory

car = car_factory.new()

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        loader = tornado.template.Loader(".")
        self.write(loader.load("web_ui/index.html").generate())

class WSHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True
    def open(self):
        print('connection opened...')
        self.write_message(json.dumps(
            {'type': 'init',
             'data': {'carSpeed': car.speed()}}))

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
        elif code.startswith('changeSpeed'):
            params = code.split(' ')[1:]
            speed_value = int(params[0])
            car.change_speed(speed_value)

    def on_close(self):
        print('connection closed...')

application = tornado.web.Application([
    (r'/ws', WSHandler),
    (r'/', IndexHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": "web_ui"}),
])

if __name__ == "__main__":
    try:
        application.listen(9000)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        car.on_exit()

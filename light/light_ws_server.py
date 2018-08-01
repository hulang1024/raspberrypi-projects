# -*- coding: utf-8 -*-

"""
    websocket服务器
"""

import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import light_group

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        loader = tornado.template.Loader(".")
        self.write(loader.load("web_ui/index.html").generate())

class WSHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True
    def open(self):
        print('connection opened...')

    def on_message(self, msg):
        if msg == 'light_count':
            self.write_message(light_count)
        elif msg.startswith('action'):
            # eg: action turn_on 1
            params = msg.split(' ')

            act = params[1]
            light_no = int(params[2])
            act_params = params[3:]

            if act == 'turn_on':
                light_group.turn_on(light_no)
            elif act == 'turn_off':
                light_group.turn_off(light_no)
            elif act == 'brightness':
                light_group.brightness(light_no, int(act_params[0]))

    def on_close(self):
        print('connection closed...')

application = tornado.web.Application([
    (r'/ws', WSHandler),
    (r'/', IndexHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": "web_ui"}),
])

if __name__ == "__main__":
    try:
        application.listen(9001)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        light_group.on_exit()

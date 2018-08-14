# -*- coding: utf-8 -*-

"""
    websocket服务器
"""

import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import asyncio
import json
from switch import Switch
from fan import Fan



class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        loader = tornado.template.Loader(".")
        self.write(loader.load("web/index.html").generate())

class WSHandler(tornado.websocket.WebSocketHandler):
    def __init__(self, *args):
        super().__init__(*args)
        self.fan = Fan(Switch(31))

    def check_origin(self, origin):
        return True

    def open(self):
        print('connection opened...')
        self.fan.set_switch_change_event_handler(
            lambda state: self.write_message(
                json.dumps({'switchState': state})))

    def write_message(self, msg):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        super().write_message(msg)

    def on_message(self, msg):
        fan = self.fan
        params = msg.split(' ')
        act = params[0]
        act_params = params[1:]

        ret = 1
        if act == 'turn_on':
            fan.turn_on()
            ret = 0
        elif act == 'turn_off':
            fan.turn_off()
            ret = 0
        elif act == 'timing_turn':
            ts = act_params[1].split(':')
            time = {'hour': int(ts[0]), 'minute': int(ts[1])}
            if act_params[0] == 'on':
                fan.timing_turn_on(time)
                ret = 0
            elif act_params[0] == 'off':
                fan.timing_turn_off(time)
                ret = 0
        elif act == 'delay_turn':
            seconds = int(act_params[1])
            if act_params[0] == 'on':
                fan.delay_turn_on(seconds)
                ret = 0
            elif act_params[0] == 'off':
                fan.delay_turn_off(seconds)
                ret = 0
        elif act == 'interval_switch':
            fan.interval_switch(int(act_params[0]))
            ret = 0

        self.write_message(str(ret))

    def on_close(self):
        print('connection closed...')

application = tornado.web.Application([
    (r'/ws', WSHandler),
    (r'/', IndexHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": "web"}),
])

if __name__ == "__main__":
    application.listen(9002)
    tornado.ioloop.IOLoop.instance().start()

import time
import threading
from datetime import datetime

class MultifunctionSwitch:
    def __init__(self, relay):
        self.relay = relay
        self.timer = None
        self.switch_change_event_handler = lambda x : x

    def __del__(self):
        self._cancel_timer()

    def set_switch_change_event_handler(self, handler):
        self.switch_change_event_handler = handler

    def turn_off(self):
        self._cancel_timer()
        self.relay.turn_off()
        self.switch_change_event_handler(0)

    def turn_on(self):
        self._cancel_timer()
        self.relay.turn_on()
        self.switch_change_event_handler(1)

    def timing_turn_on(self, time):
        """
        :param time 字典时间, 如 {hour: 23, minute: 10}
        """
        self._timing_turn(time, self.delay_turn_on)

    def timing_turn_off(self, time):
        self._timing_turn(time, self.delay_turn_off)

    def delay_turn_on(self, seconds):
        self._cancel_timer()
        self.timer = threading.Timer(seconds, lambda: self.turn_on())
        self.timer.start()

    def delay_turn_off(self, seconds):
        self._cancel_timer()
        self.timer = threading.Timer(seconds, lambda: self.turn_off())
        self.timer.start()

    def interval_switch(self, seconds):
        self._cancel_timer()
        self.timer = threading.Timer(seconds, self._loop, (seconds,))
        self.timer.start()

    def _loop(self, seconds):
        if self.relay.is_on():
            self.relay.turn_off()
        else:
            self.relay.turn_on()

        self.interval_switch(seconds)

    def _cancel_timer(self):
        if self.timer != None:
            self.timer.cancel()

    def _timing_turn(self, time, delay_turn_func):
        now = datetime.now()
        minutes = (time['hour'] * 60 + time['minute']) - (now.hour * 60 + now.minute)

        delay_turn_func(minutes * 60)


if __name__ == '__main__':
    switch = MultifunctionSwitch(LowCloseRelay(31))
    time.sleep(2)
    switch.turn_on()

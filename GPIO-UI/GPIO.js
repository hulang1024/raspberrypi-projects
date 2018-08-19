//GPIO模拟器
function GPIO(pinBoard) {
  var conf = {};//配置功能,输入=1还是输出=0
  var data = {};//数据读写寄存器
  var nowMode;

  var self = {
    setmode: function(mode) {
      nowMode = mode;
    },

    setup: function(pinNo, io) {
      conf[pinNo] = io;
    },

    output: function(pinNo, n) {
      if (conf[pinNo] != 0) {
        alert('emm')
        return;
      }

      data[pinNo] = n;

      pinBoard.output(pinNo, n);
    },

    input: function(pinNo) {
      if (conf[pinNo] != 1) {
        alert('emm')
        return;
      }

      return data[pinNo];
    },

    _read: function(pinNo) {
      return data[pinNo];
    },

    cleanup: function() {}
  };

  pinBoard.pins.forEach(function(pin, boardPinNo) {
    if (pin instanceof GPIOPin)
      self.setup(boardPinNo, GPIO.IN);
  });

  return self;
}
GPIO.IN = 1;
GPIO.OUT = 0;

GPIO.BOARD =  1;

GPIO.LOW = 0;
GPIO.HIGH = 1;

//可画的对象

function Pin(funcName, color) {
  this.funcName = funcName;
  this.color = color;

  var outer = document.createElement('div');
  outer.className = 'pin';
  outer.title = funcName;
  outer.style.backgroundColor = color;
  var inner = document.createElement('div');
  outer.appendChild(inner);

  this.div = outer;
}

function VccPin(v) {
  Pin.call(this, v + 'V', v > 3.3 ? '#ea3323' : '#b9433d');
  this.v = v;
}

function GndPin() {
  Pin.call(this, 'GND', 'black');
}

function GPIOPin(gpioNo, v) {
  Pin.call(this, 'GPIO.' + gpioNo, '#50b133');
}

var pins = [];
pins[1] = new VccPin(3.3);
pins[2] = new VccPin(5);
pins[3] = new Pin('SDA.1', '#6da9f8');
pins[4] = new VccPin(5);
pins[5] = new Pin('SDL.1', '#6da9f8');
pins[6] = new GndPin();
pins[7] = new GPIOPin(7);
pins[8] = new Pin('TXD.0', '#f19b46');
pins[9] = new GndPin();
pins[10] = new Pin('RXD.0', '#f19b46');
pins[11] = new GPIOPin(0, 0);
pins[12] = new GPIOPin(1, 0);
pins[13] = new GPIOPin(2, 0);
pins[14] = new GndPin();
pins[15] = new GPIOPin(3, 0);
pins[16] = new GPIOPin(4, 0);
pins[17] = new VccPin(3.3);
pins[18] = new GPIOPin(5, 0);
pins[19] = new Pin('MOSI', '#cb63f7');
pins[20] = new GndPin();
pins[21] = new Pin('MISO', '#cb63f7');
pins[22] = new GPIOPin(6, 0);
pins[23] = new Pin('SCLK', '#cb63f7');
pins[24] = new Pin('CE0', '#cb63f7');
pins[25] = new GndPin();
pins[26] = new Pin('CE1', '#cb63f7');
pins[27] = new Pin('SDA.0', '#f7cf46');
pins[28] = new Pin('SCL.0', '#f7cf46');
pins[29] = new GPIOPin(21, 1);
pins[30] = new GndPin();
pins[31] = new GPIOPin(22, 1);
pins[32] = new GPIOPin(26, 0);
pins[33] = new GPIOPin(23, 0);
pins[34] = new GndPin();
pins[35] = new GPIOPin(24, 0);
pins[36] = new GPIOPin(27, 0);
pins[37] = new GPIOPin(25, 0);
pins[38] = new GPIOPin(28, 0);
pins[39] = new GndPin();
pins[40] = new GPIOPin(29, 0);

var pinBoard = new PinBoard();
var gpio = new GPIO(pinBoard);
pinBoard.connectGPIO(gpio);
gpio.setmode(GPIO.BOARD);

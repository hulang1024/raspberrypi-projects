
var GPIO = (function() {
  var nowMode;

  return {
    IN: 1,
    OUT: 2,

    BOARD: 1,

    LOW: 0,
    HIGH: 1,

    setmode: function(mode) {
      nowMode = mode;
    },

    setup: function(pinNo, io) {
      pins[pinNo].setup(io);
    },

    output: function(pinNo, bin) {
    },

    cleanup: function() {}
  };
})();
GPIO.setmode(GPIO.BOARD);

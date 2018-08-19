function initAllPins() {
  var pinBoard = document.getElementById('pin-board');
  pins.forEach(function(pin, i) {
    pinBoard.appendChild(pin.div);
  });
}

initAllPins();

var isMobile = !navigator.userAgent || /Android|webOS|iPhone|iPod|BlackBerry/i.test(navigator.userAgent);

$(function($){
  var hostname = location.hostname || "localhost";
  var socket = new WebSocket("ws://" + hostname + ":9000/ws");

  var speed = 0;

  socket.onopen = function(){
    alert("连接服务器成功!");
  }

  socket.onmessage = function(msg) {
    ret = JSON.parse(msg.data || msg);
    switch (ret.type) {
      case 'init':
        speed = ret.data.carSpeed;
        $('#curr-speed-number').val(speed);
        break;
    }
  }

  socket.onclose = function(){
  }


  if (!isMobile) {
    $('#keyboard-info').show();
  }

  document.oncontextmenu = function(){
    event.returnValue = false;
  };

  var ui = {};
  ui.Button = function(dom) {
    var handlers = {};

    $(dom)
      .mousedown(function() {
        $(this).addClass('ui-button-down');
      })
      .mouseup(function() {
        $(this).removeClass('ui-button-down');
      })
      .click(function() {
        handlers['click']();
      });

    this.onClick = function(f) {
      handlers['click'] = f;
    }
  }

  new ui.Button('.ctrl-dir .fore').onClick(function() {
    sendCode('fore');
  });

  new ui.Button('.ctrl-dir .back').onClick(function() {
    sendCode('back');
  });

  new ui.Button('.ctrl-dir .left').onClick(function() {
    sendCode('turnLeft');
  });

  new ui.Button('.ctrl-dir .right').onClick(function() {
    sendCode('turnRight');
  });

  new ui.Button('.ctrl-dir .stop').onClick(function() {
    sendCode('stop');
  });

  new ui.Button('#inc-speed').onClick(function() {
    changeSpeed(+1);
  });
  new ui.Button('#dec-speed').onClick(function() {
    changeSpeed(-1);
  });

  new ui.Button('#set-speed').onClick(function() {
    speed = + $('#curr-speed-number').val();
    changeSpeed(0);
  });

  function changeSpeed(v) {
    speed += 1 * v;
    if (speed > 100)
      speed = 100;
    if (speed < 0)
      speed = 0;
    sendCode('changeSpeed ' + speed);
    $('#curr-speed-number').val(speed);
  }

  document.addEventListener('keydown', function(event) {
    switch (event.keyCode) {
    case 38:
    case 87:
      sendCode('fore');
      break;
    case 40:
    case 83:
      sendCode('back');
      break;
    case 37:
    case 65:
      sendCode('turnLeft');
      break;
    case 39:
    case 68:
      sendCode('turnRight');
      break;
    case 32:
      sendCode('stop');
      break;
    }
  });

  function sendCode(code) {
    console.log('send code:', code);
    socket.send(code);
  }

});

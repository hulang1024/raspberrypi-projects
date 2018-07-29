var isMobile = !navigator.userAgent || /Android|webOS|iPhone|iPod|BlackBerry/i.test(navigator.userAgent);

$(function($){
  var hostname = location.hostname || "localhost";
  var socket = new WebSocket("ws://" + hostname + ":9000/ws");
  socket.onopen = function(){
    alert("连接服务器成功!");
  }

  socket.onmessage = function(msg){
    console.log(msg.data);
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

  new ui.Button('.ctrl-buttons .fore').onClick(function() {
    sendCode('fore');
  });

  new ui.Button('.ctrl-buttons .back').onClick(function() {
    sendCode('back');
  });

  new ui.Button('.ctrl-buttons .left').onClick(function() {
    sendCode('turnLeft');
  });

  new ui.Button('.ctrl-buttons .right').onClick(function() {
    sendCode('turnRight');
  });

  new ui.Button('.ctrl-buttons .stop').onClick(function() {
    sendCode('stop');
  });

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

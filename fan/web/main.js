$(function() {
  var hostname = location.hostname || "localhost";
  var socket = new WebSocket("ws://" + hostname + ":9002/ws");
  socket.onopen = function(){
  }

  socket.onmessage = function(msg){
    ret = JSON.parse(msg.data || msg);
    if (typeof ret == 'number') {
      if (ret == 0) {
        $('#op-info').addClass('op-succeed').text('操作成功').show();
      } else {
        $('#op-info').addClass('op-failed').text('操作失败').show();
      }
      $('#op-info').fadeOut(2000);
    } else {
      if (ret.switchState) {
        honeySwitch.showOn('#switch-1');
      } else {
        honeySwitch.showOff('#switch-1');
      }
    }
  }

  socket.onclose = function(){
  }

  switchEvent('#switch-1',
    function() {
      socket.send('turn_on');
    },
    function() {
      socket.send('turn_off');
    });

  ['on', 'off'].forEach(function(otype) {
    (function(otype) {
      $('#set-timing-turn-' + otype).click(function() {
        var time = $('#timing-turn-' + otype + '-time').val();
        if (!time)
          return;
        socket.send('timing_turn' + ' ' + otype + ' ' + time);
      });

      $('#set-delay-turn-' + otype).click(function() {
        var time = $('#delay-turn-' + otype + '-time').val();
        if (!time)
          return;
        socket.send('delay_turn' + ' ' + otype + ' ' + time);
      });
    })(otype);
  });

  $('#set-interval-switch').click(function() {
    var time = $('#interval-switch-time').val();
    if (!time)
      return;
    socket.send('interval_switch' + ' ' + time);
  });
});

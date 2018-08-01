$(function() {
  var hostname = location.hostname || "localhost";
  var socket = new WebSocket("ws://" + hostname + ":9001/ws");
  socket.onopen = function(){
  }

  socket.onmessage = function(msg){
    console.log(msg.data);
  }

  socket.onclose = function(){
  }

  for (var i = 1; i <= 3; i++) {
    (function(n) {
    switchEvent("#switch-" + n,
      function() {
        socket.send('action turn_on ' + n);
        $('#range-' + n).val(255);
      },
      function() {
        socket.send('action turn_off ' + n);
        $('#range-' + n).val(0);
  	  });

      $('#range-' + n).change(function() {
        socket.send('action brightness ' + n + ' ' + this.value);
      })
    })(i);
  }
});

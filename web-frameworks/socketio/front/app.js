$(() => {
  const socket = io("http://127.0.0.1:5000");

  socket.on('connected', (something) => {
    console.log("CONNECTED RECEIVED")
    console.log(something);
  })

  socket.on('data-processing-done', (bla) => {
    console.log("DATA-PROCESSING RECEIVED")
    console.log(bla);
  })

  $("#thebutton").click(() => {
    console.log("Pushed");
    socket.emit('process-data', "FWAFAWFWF");
  });
});

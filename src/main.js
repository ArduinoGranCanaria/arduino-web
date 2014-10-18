function cambiarLuminosidad(msg)
{
  var lum = parseFloat(msg) / 1024.0;
  $('h1').css ('opacity', lum);
}

function loop ()
{
  $.ajax("/luminosidad").done(cambiarLuminosidad);
}

setInterval(loop, 1000);

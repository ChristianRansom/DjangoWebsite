/**
 * http://pixelhunter.me/
 *
 * text {String} - printing text
 * n {Number} - from what letter to start
 */
var running = false;
function typeWriter(text, n) {
  if (n < (text.length)) {
    document.getElementById("typewriter").textContent = text.substring(0, n+1);
    n++;
    setTimeout(function() {
      typeWriter(text, n)
    }, 10);
  }
  else {
    running = false;
  }
}

$(document).on('scroll', function() {
    if( $(this).scrollTop() + 500 >= $('#typewriter').position().top) {
        if( $(this).scrollTop() + 300 <= $('#typewriter').position().top) {
           if(running === false){
                running = true;
                typeWriterHelper();
            }
        }
    }
});

function typeWriterHelper(){
    var text = document.getElementById("typewriter").textContent;
    typeWriter(text, 0);
}

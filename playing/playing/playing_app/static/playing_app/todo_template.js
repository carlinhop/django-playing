
$(document).ready(function(){

   $(".todo").hover(changeBackgroundOn,changeBackgroundOoff);

});

function changeBackgroundOn(){$(this).css("background-color","#a2d3c2")}

function changeBackgroundOoff(){$(this).css("background-color","white")}

$(document).ready(function(){

   $(".todo").hover(changeBackgroundOn,changeBackgroundOoff);
   
   $(".search").focusin();

});

function changeBackgroundOn(){$(this).css("background-color","#a2d3c2")}

function changeBackgroundOoff(){$(this).css("background-color","white")}

//This function gets all users from the db and shows them in the console--Practicing ajax
function test(){  $.get( "http://development-carlinhop.c9.io/home/users", function( data ) {
                  $(".search").val("Hola");
                  var usernames = data;
                  usernames.forEach(function(username){$(".options-test").append("<p>"+username.username+"</p>")});
                  
                  });}



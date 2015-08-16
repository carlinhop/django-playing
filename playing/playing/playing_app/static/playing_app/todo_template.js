
$(document).ready(function(){

   //$(".todo").hover(changeBackgroundOn,changeBackgroundOoff);
   
   $(".glyphicon").hover(changeGlyphiconOn,changeGlyphiconOff);
   $(".form-group").hover(editFieldOn,editFieldOff);
   $(".form-group").click(function(){$(this).prop('disabled', false)});

});

function changeBackgroundOn(){$(this).css("background-color","#a2d3c2")}

function changeBackgroundOoff(){$(this).css("background-color","white")}

//This function gets all users from the db and shows them--Practicing ajax
function test(){  $.get( "http://development-carlinhop.c9.io/home/users", function( data ) {
                  $(".search").val("Hola");
                  var usernames = data;
                  usernames.forEach(function(username){$(".options-test").append("<p>"+username.username+"</p>")});
                  
                  });}


function changeGlyphiconOn()
{
   $(this).removeClass("glyphicon-remove").addClass("glyphicon-ok");
}


function changeGlyphiconOff()
{
   $(this).removeClass("glyphicon-ok").addClass("glyphicon-remove");
}

function editFieldOn()
{
   $("i").addClass("form-control-feedback glyphicon glyphicon-pencil");
}

function editFieldOff()
{
   $("i").removeClass("form-control-feedback glyphicon glyphicon-pencil");
}
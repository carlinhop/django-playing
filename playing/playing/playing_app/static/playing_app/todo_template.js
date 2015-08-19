
$(document).ready(function(){

   //$(".todo").hover(changeBackgroundOn,changeBackgroundOoff);
   
   $(".glyphicon").click(function()
   {
      if ($(this).hasClass("glyphicon-remove"))
      {
         changeGlyphiconOn($(this));
         
      }
      
      else
      {
         changeGlyphiconOff($(this));
      }
   });
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


function changeGlyphiconOn(element)
{
   element.removeClass("glyphicon-remove").addClass("glyphicon-ok");
   
   var element_id = element.attr("id");
   
   $("."+element_id).css("text-decoration", "line-through");
   
   // using jQuery
   function getCookie(name) {
       var cookieValue = null;
       if (document.cookie && document.cookie != '') {
           var cookies = document.cookie.split(';');
           for (var i = 0; i < cookies.length; i++) {
               var cookie = jQuery.trim(cookies[i]);
               // Does this cookie string begin with the name we want?
               if (cookie.substring(0, name.length + 1) == (name + '=')) {
                   cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                   break;
               }
           }
       }
       return cookieValue;
   }
   var csrftoken = getCookie('csrftoken');
   
   $.ajax({type:"POST",url:"http://development-carlinhop.c9.io/home/todo-done",
   headers:{"X-CSRFToken":csrftoken},data:{id:element_id}}).done(function(){console.log("posted");});
}


function changeGlyphiconOff(element)
{
   element.removeClass("glyphicon-ok").addClass("glyphicon-remove");
      var element_id = element.attr("id");
   
   $("."+element_id).css("text-decoration", "none");
 // using jQuery
   function getCookie(name) {
       var cookieValue = null;
       if (document.cookie && document.cookie != '') {
           var cookies = document.cookie.split(';');
           for (var i = 0; i < cookies.length; i++) {
               var cookie = jQuery.trim(cookies[i]);
               // Does this cookie string begin with the name we want?
               if (cookie.substring(0, name.length + 1) == (name + '=')) {
                   cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                   break;
               }
           }
       }
       return cookieValue;
   }
   var csrftoken = getCookie('csrftoken');
   
   $.ajax({type:"POST",url:"http://development-carlinhop.c9.io/home/todo-done",
   headers:{"X-CSRFToken":csrftoken},data:{id:element_id}}).done(function(){console.log("posted");});   
   
}

function editFieldOn()
{
   $("i").addClass("form-control-feedback glyphicon glyphicon-pencil");
}

function editFieldOff()
{
   $("i").removeClass("form-control-feedback glyphicon glyphicon-pencil");
}



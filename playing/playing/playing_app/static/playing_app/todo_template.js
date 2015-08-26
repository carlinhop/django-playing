
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
   $(".todo_created").change(function()
   {
      saveDate($(this));
   });

});

//Functions not in use

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
   
   //getCookie is defined in static/csrf.js
   var csrftoken = getCookie('csrftoken');
   
   $.ajax({type:"POST",url:"http://development-carlinhop.c9.io/home/todo-done",
   headers:{"X-CSRFToken":csrftoken},data:{id:element_id}}).done(function(){console.log("posted");});
}


function changeGlyphiconOff(element)
{
   element.removeClass("glyphicon-ok").addClass("glyphicon-remove");
      var element_id = element.attr("id");
   
   $("."+element_id).css("text-decoration", "none");
   //getCookie is defined in static/csrf.js
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


function saveDate(element)
{
   var element_id = element.attr("id");
   var element_value = element.val()
   //getCookie is defined in static/csrf.js
   var csrftoken = getCookie('csrftoken');
   
   $.ajax({type:"POST",url:"http://development-carlinhop.c9.io/home/todo-date",
   headers:{"X-CSRFToken":csrftoken},data:{id:element_id,value:element_value}}).done(function(){console.log("posted");});
}
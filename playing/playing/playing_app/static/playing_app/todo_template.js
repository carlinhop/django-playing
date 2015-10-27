
$(document).ready(function(){
   
   //Defining functions
   
   
   function btnDanger(event)
                           {
                              $(this).removeClass("btn-default").addClass("btn-danger");
                              
                           }
   
   
   
   function btnDefault(event)
                           {
                              $(this).removeClass("btn-danger").addClass("btn-default");
                              
                           }
   
 
 function removeAsignee(element,todo_id)
{
   //getCookie is defined in static/csrf.js
   var csrftoken = getCookie('csrftoken');
   
   $.ajax({type:"POST",url:"http://development-carlinhop.c9.io/home/remove-asignee",
   headers:{"X-CSRFToken":csrftoken},data:{"username":element,"todo_id":todo_id}}).done(function(data){console.log("posted");});
   
}
 
 
   
function saveAsignee(element)
{
   var element_id = element.attr("id");
   var element_value = element.val();
   var element_id_number = element_id.substr(8,element_id.length-1);
   //getCookie is defined in static/csrf.js
   var csrftoken = getCookie('csrftoken');
   
   $.ajax({type:"POST",url:"http://development-carlinhop.c9.io/home/todo-asignee",
   headers:{"X-CSRFToken":csrftoken},data:{id:element_id,value:element_value}}).done(function(data){var target =  $("#search"+element_id.substring(7)+">.responsibles-space");target.empty();data.map(function(datum){target.append(" <input type='submit' id ='"+"responsible-"+element_id_number+"' class= 'responsible btn btn-default' value ='"+datum+"'/>");});element.blur();
   
   
   
   $(".responsible").hover(btnDanger,btnDefault); 
                           
   $(".responsible").click(function(){
      
      $(this).addClass("animated zoomOut");
      var asigneeName = $(this).val();
      var todo_id = $(this).attr("id");
      
      
      
      removeAsignee(asigneeName,todo_id);
   });                        
      
   });
   
   
}



   //This function gets all users from the db and shows them--Practicing ajax
function test(name,value,object)
{
   
   
   $.get( "http://development-carlinhop.c9.io/home/users",{value:value}, function( data ) 
   {
   
      
      
         
         var usernames = data;
         $("option").remove();
         if (usernames[0].username!=="Nothing to show")
         {
            usernames.forEach(function(username){$("#results").append("<option value ="+ username.username+">");});
            
         }
         
   });
}


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
   var element_value = element.val();
   //getCookie is defined in static/csrf.js
   var csrftoken = getCookie('csrftoken');
   
   $.ajax({type:"POST",url:"http://development-carlinhop.c9.io/home/todo-date",
   headers:{"X-CSRFToken":csrftoken},data:{id:element_id,value:element_value}}).done(function(){console.log("posted");});
}





   $(".glyphicon").css( "cursor", "pointer" );
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
   $(".add").hover(editFieldOn,editFieldOff);
   
   $(".form-group").click(function(){$(this).prop('disabled', false)});
   $(".todo_created").change(function()
   {
      saveDate($(this));
   });
   $(".responsibles-search").keyup(function(event)
   {  
      var key_event=event.keyCode;
      
      if (key_event!="40" && key_event!="38"){
      var name = $(this).attr("name");
      var value = $(this)[0].value;
      var  x = this;
      
      test(name,value,x);
      }
      
      
   });
   
   $(".responsibles-search").keydown(function(event)
   {
      var key_event= event.keyCode;
      
      if(key_event=="13")
      {
         saveAsignee($(this));
      }
   });
   
   $(".responsible").hover(btnDanger,btnDefault);
                           
   $(".delete").hover(btnDanger,btnDefault);                        

   $(".responsible").click(function()
   {
      var asigneeName = $(this).val();
      var todo_id = $(this).attr("id");
      
      $(this).addClass("animated zoomOut");
      
      removeAsignee(asigneeName,todo_id);
       
   });
   

//end
});




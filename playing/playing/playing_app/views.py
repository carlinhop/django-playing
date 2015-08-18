from django.shortcuts import render, redirect,get_object_or_404
from django.conf import settings   
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.views.generic import ListView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.core import serializers
from .models import Todo
from .forms import CreateTodoForm,CreateEasyTodoForm,LoginForm,RegisterForm,GetResetPasswordLink,ResetPassword




def todo_list_view(request):
    user = request.user
    if request.method == "POST":
        if user.is_authenticated():
            form = CreateEasyTodoForm(data = request.POST)
            
            if form.is_valid():
                todo = form.save(commit = False)
                default_user = User.objects.get(username = user)
                todo.save()
                
                todo.todo_responsibles.add(default_user)
                todo.save()
                return redirect("list")
            else:
                return HttpResponse("not working")
            
                
    else:
        
        todos = Todo.objects.all().filter(todo_responsibles__username=user)
        
        context = {"todos": todos}
        
        if user.is_authenticated():
            context["user"] = user.get_username()
            return render(request, "playing_app/todo_template.html",context)
        else:
            return redirect("login")


def todo_create(request):
    if request.method == "POST":
        form = CreateTodoForm(data = request.POST)
        
        
        
        
        if form.is_valid():
            todo = form.save(commit = False)
            
            
            todo.save()
            responsibles = request.POST.getlist("todo_responsibles")
            default_user = User.objects.get(username = request.user)
            todo.todo_responsibles.add(default_user)
            
            for id in responsibles:
                
                people = User.objects.get(pk = int(id))
            
            
                todo.todo_responsibles.add(people)
            
            
            return redirect("list")
        
            

    else:
        form = CreateTodoForm()
        
        context = {"form": form,"create": True}
        return render(request,"playing_app/form.html",context)
        

def todo_edit(request):
     
    todo_id = request.GET.get("id")
    if Todo.objects.get(pk = todo_id).todo_responsibles.all():
        print("OK")
    else:
        print("no responsibles found")
    data = {"todo_text":Todo.objects.get(id = todo_id).todo_text,"todo_responsibles":Todo.objects.get(id = todo_id).todo_responsibles.all(),"todo_created":Todo.objects.get(id = todo_id).todo_created}
    
    form = CreateTodoForm(data)
    
    context = {"form":form, "id":todo_id}
    if request.method == "POST":
        
        form = CreateTodoForm(data = request.POST)
        
        
        
        if form.is_valid():
            todo = form.save(commit = False)
            todo.id = todo_id
            
            todo.save()

            todo.todo_responsibles.clear()
            responsibles = request.POST.getlist("todo_responsibles")
            for id in responsibles:
                
                people = User.objects.get(pk = int(id))
            
            
                todo.todo_responsibles.add(people)
            
            
            return redirect("list")
    else:
        
        return render(request,"playing_app/form.html",context)
            
            
            
def todo_delete(request):
    
        
    todo_id = request.POST.get("id")
    
    target = Todo.objects.filter(id = todo_id)
    target.delete()
    
        
    return redirect("list")
    
    





def login_user(request):
    if request.method == "POST":
        print(request)
        form = LoginForm(data = request.POST)
        context = {"form":form,"create":True}
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("list")
        else:
            return redirect("reset_link")
        
    else:
        form = LoginForm()
        context = {"form":form,"create":True}
        return render(request,"playing_app/login.html",context)
        


def logout_user(request):
    logout(request)
    print(request)
    return redirect("login")



def register(request):
    if request.method == "POST":
        form = RegisterForm(data = request.POST)
        if form.is_valid:
            user = User.objects.filter(username = request.POST["username"])
            
            if not user:
                user = User.objects.create_user(username=request.POST["username"],password = request.POST["password"],email = request.POST["email"])
                user.save()
                
                send_mail('You have been registered!!!', 'yuujiiiiiii', settings.EMAIL_HOST_USER,[request.POST['email']], fail_silently=False)
                login_user(request)
                return redirect("list")
            else:
                return HttpResponse("User already registered")
    else:
        form = RegisterForm()
        context = {"form":form,"create":True}
        return render(request,"playing_app/login.html",context)





def reset_password(request):
    if request.method == "POST":
        user = User.objects.filter(email = request.POST.get("email",""))
        
        if user:
            form = ResetPassword(data = request.POST)
            if form.is_valid:
                user[0].set_password(request.POST.get("password",""))
                user[0].save()
                
                return redirect("login")
    else:
        email = request.GET.get("email","")
        data = {"email":email}
        form = ResetPassword(data)
        context = {"form":form,"create":True}
        return render(request,"playing_app/login.html",context)

    
def get_reset_password_link(request):
    if request.method == "POST":
        
        form = GetResetPasswordLink(data = request.POST)
        if form.is_valid:
            user = User.objects.filter(email = request.POST["email"])
            
            if user:
                
                send_mail("Reset your password", "http://development-carlinhop.c9.io/home/reset-password?email="+str(user[0].email ), settings.EMAIL_HOST_USER,[request.POST["email"]], fail_silently=False)
                return HttpResponse("Check your email buddy")
        else:
            return HttpResponse("User not registered")
    else:
        form = GetResetPasswordLink()
        context = {"form":form,"create":True}
        return render(request,"playing_app/login.html",context)
        
        
        
#JSON views to serve AJAX

def get_users(request):
    """This is for getting all the users in JSON format"""
    #You have to convert it to a list to avoid the 20 record limit
    users = list(User.objects.values("username"))
    
    return JsonResponse(users, safe = False)

from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Todo,Responsible
from .forms import CreateTodoForm,CreateResponsibleForm,Login



def todo_list_view(request):
    todos = Todo.objects.all()
    
    context = {"todos": todos}
    return render(request, "playing_app/todo_template.html",context)
    


def todo_create(request):
    if request.method == "POST":
        form = CreateTodoForm(data = request.POST)
        
        
        
        
        if form.is_valid():
            todo = form.save(commit = False)
            
            
            todo.save()
            responsibles = request.POST.getlist("todo_responsibles")
            for id in responsibles:
                
                people = Responsible.objects.get(pk = int(id))
            
            
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
    data = {"todo_text":Todo.objects.get(id = todo_id).todo_text,"todo_responsibles":Todo.objects.get(pk = todo_id).todo_responsibles.all(),"todo_created":Todo.objects.get(id = todo_id).todo_created}
    
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
                
                people = Responsible.objects.get(pk = int(id))
            
            
                todo.todo_responsibles.add(people)
            
            
            return redirect("list")
    else:
        
        return render(request,"playing_app/form.html",context)
            
            
            
def todo_delete(request):
    
        
    todo_id = request.POST.get("id")
    
    target = Todo.objects.filter(id = todo_id)
    target.delete()
    
        
    return redirect("list")
    
    


def create_responsible(request):
    if request.method == "POST":
        form = CreateResponsibleForm(data = request.POST)
        if form.is_valid():
            responsible = form.save(commit = False)
            responsible.save()
            return redirect("responsible")
            
    else:
        responsibles = Responsible.objects.all()
        form = CreateResponsibleForm()
        context = {"form": form, "create": True,"responsibles":responsibles}
        return render(request,"playing_app/responsibles.html",context)
        
        

def delete_responsible(request):

    if request.method == "POST":
        responsible_id = request.POST.get("id")
        responsible = Responsible.objects.filter(pk = responsible_id)
        print(responsible_id)
        responsible.delete()
        
        return redirect("responsible")
    else:
        return redirect("responsible")


def login(request):
    if request.method == "POST":
        form = Login(data = request.POST)
        if form.is_valid:
            
            
            user = User.objects.create_user(username=request.POST["username"],password = request.POST["password"])
            user.save()
            print(user)
            return redirect("list")
    else:
        form = Login()
        context = {"form":form,"create":True}
        return render(request,"playing_app/login.html",context)

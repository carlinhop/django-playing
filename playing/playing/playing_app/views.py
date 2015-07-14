from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from django.core.urlresolvers import reverse
from .models import Todo,Responsible
from .forms import CreateTodoForm,CreateResponsibleForm


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
            responsible = Responsible.objects.get(pk = request.POST.get("todo_responsibles"))
            todo.todo_responsibles.add(responsible)
            
            
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
    data = {"todo_text":Todo.objects.get(id = todo_id).todo_text,"todo_responsibles":Todo.objects.get(pk = todo_id).todo_responsibles.all()}
    
    form = CreateTodoForm(data)
    
    context = {"form":form, "id":todo_id}
    if request.method == "POST":
        form = CreateTodoForm(data = request.POST)
        
        
        
        if form.is_valid():
            todo = form.save(commit = False)
            todo.id = todo_id
            
            todo.save()
       
            responsible = Responsible.objects.get(pk = request.POST.get("todo_responsibles"))
            todo.todo_responsibles.add(responsible)
            
            
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
        
        form = CreateResponsibleForm()
        context = {"form": form, "create": True}
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

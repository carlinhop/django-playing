from django import forms
from django.forms import widgets
from .models import Todo,Responsible


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["todo_text", "todo_done", "id", "todo_responsibles"]
        widgets = {"todo_responsibles" : widgets.CheckboxSelectMultiple()}
               
        
class CreateResponsibleForm(forms.ModelForm):
    class Meta:
        model = Responsible
        fields = ["responsible_name"]
        
        
   
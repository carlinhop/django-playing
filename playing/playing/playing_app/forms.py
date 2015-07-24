from django import forms
from django.forms import widgets
from .models import Todo,Responsible


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["todo_text", "todo_done", "id", "todo_responsibles","todo_created"]
        widgets = {"todo_responsibles" : widgets.CheckboxSelectMultiple(), "todo_created": widgets.DateInput()}
               
        
class CreateResponsibleForm(forms.ModelForm):
    class Meta:
        model = Responsible
        fields = ["responsible_name"]
        
        

class Login(forms.Form):
    username = forms.CharField(label = "Username", max_length = 100)
    
        
   
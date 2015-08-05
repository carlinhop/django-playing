from django import forms
from django.forms import widgets
from .models import Todo


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["todo_text", "todo_done", "id", "todo_responsibles","todo_created"]
        widgets = {"todo_responsibles" : widgets.CheckboxSelectMultiple(), "todo_created": widgets.DateInput()}
               
        

        
        

class Login(forms.Form):
    username = forms.CharField(label = "Username", max_length = 20)
    password = forms.CharField(label = "Password", max_length = 10, widget=forms.PasswordInput)
    
    
        
   
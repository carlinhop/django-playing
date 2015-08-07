from django import forms
from django.forms import widgets
from .models import Todo


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["todo_text", "todo_done", "id", "todo_responsibles","todo_created"]
        widgets = {"todo_responsibles" : widgets.CheckboxSelectMultiple(), "todo_created": widgets.DateInput()}
               
        

        
        

class RegisterForm(forms.Form):
    username = forms.CharField(label = "Username", max_length = 20)
    password = forms.CharField(label = "Password", max_length = 10, widget=forms.PasswordInput)
    email = forms.CharField(label = "email", max_length = 20, widget = forms.EmailInput)
    
    
        
class LoginForm(forms.Form):
    username = forms.CharField(label = "Username", max_length = 20)
    password = forms.CharField(label = "Password", max_length = 10, widget=forms.PasswordInput)   
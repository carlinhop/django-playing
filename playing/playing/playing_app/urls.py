from django.conf.urls import  url
from . import views



urlpatterns = [
    
    url(r'^list$', views.todo_list_view, name = "list"),
    url(r'^create$', views.todo_create, name = "create"),
    url(r'^edit$', views.todo_edit, name = "edit"),
    url(r'^delete',views.todo_delete, name = "delete"),
    url(r'^responsible',views.create_responsible, name = "responsible"),
    url(r'^removeres$',views.delete_responsible, name = "delete-responsible"),
]

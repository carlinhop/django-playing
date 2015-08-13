from django.conf.urls import  url
from . import views



urlpatterns = [
    
    url(r'^list$', views.todo_list_view, name = "list"),
    url(r'^create$', views.todo_create, name = "create"),
    url(r'^edit$', views.todo_edit, name = "edit"),
    url(r'^delete',views.todo_delete, name = "delete"),
    
    
    url(r'^register$',views.register, name = "register"),
    url(r'^login',views.login_user, name = "login"),
    url(r'^logout',views.logout_user, name = "logout"),
    url(r'^users',views.get_users, name = "users"),
    url(r'^reset',views.reset_password, name = "reset"),
    
]

from django.conf.urls import  url
from . import views



urlpatterns = [
    
    url(r'^list$', views.todo_list_view, name = "list"),
    
    url(r'^edit$', views.todo_edit, name = "edit"),
    url(r'^delete',views.todo_delete, name = "delete"),
    
    
    url(r'^register$',views.register, name = "register"),
    url(r'^login',views.login_user, name = "login"),
    url(r'^logout',views.logout_user, name = "logout"),
    url(r'^users',views.get_users, name = "users"),
    url(r'^reset-link$',views.get_reset_password_link, name = "reset_link"),
    url(r'^reset-password',views.reset_password, name = "reset_password"),
    url(r'^todo-done',views.todo_done_AJAX, name ="todo-done"),
    url(r'^todo-date',views.todo_date_AJAX, name ="todo-date"),
    url(r'^todo-asignee',views.todo_asignee_AJAX, name ="todo-asignee"),
    url(r'^remove-asignee',views.remove_asignee_AJAX, name ="remove-asignee"),
    
]

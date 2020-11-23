from django.urls import path
from .views import TasksListView,ProjectListView,RoleListView
app_name = 'tasks'
urlpatterns = [
    path('', TasksListView.as_view()),
    path('project', ProjectListView.as_view()),
    path('role',RoleListView.as_view())
    
]
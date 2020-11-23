from django.conf.urls import url
from . import views


urlpatterns = [
    url('api/users', views.UserCreate.as_view(), name='account-create'),
    url('tasks',views.TaskCreate.as_view(), name='tasks-create'),
    url('project',views.ProjectCreate.as_view(),name='project-create'),
    
]
from django.urls import path
from project import views

app_name = 'project'

urlpatterns = [
    path('', views.projects, name='all'),
    path('project-details', views.details, name='details'),
]
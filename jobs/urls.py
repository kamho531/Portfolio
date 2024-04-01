from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/<int:job_id>', views.jobsdetail, name='detail'),
    
]
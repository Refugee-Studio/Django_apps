from django.urls import path
from app_jobs_parser import views

urlpatterns = [
    path('', views.jobs_input),
    path('jobs_results/', views.jobs_parser, name='jobs_results'),
    ]

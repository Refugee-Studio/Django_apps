from django.urls import path
from jobs_parser import views

urlpatterns = [
    path('', views.jobs_input),
    path('jobs_parser/', views.jobs_parser, name='jobs_parser'),
    path('jobs_results/', views.jobs_results, name='jobs_results'),
]

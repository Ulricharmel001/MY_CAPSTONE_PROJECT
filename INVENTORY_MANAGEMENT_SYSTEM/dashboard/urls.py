from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome_view, name='welcome_view'),
    path('dashboard/', views.dashboard_view, name='dashboard_view'),





]



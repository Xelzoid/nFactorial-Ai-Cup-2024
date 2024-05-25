from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register', views.register, name='register'),
    path('loginfunc', views.loginfunc, name='loginfunc'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('mealplan/', views.mealplan, name='mealplan'),
]

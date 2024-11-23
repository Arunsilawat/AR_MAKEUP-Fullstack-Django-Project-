
from django.urls import path,include
from app import views
urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
]
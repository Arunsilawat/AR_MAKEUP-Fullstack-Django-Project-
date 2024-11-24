
from django.urls import path,include
from app import views
urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('datapost/', views.datapost, name='datapost'),
    path("addtocard/<int:pk>",views.addtocard,name='addtocard'),
    path("cart/",views.cart,name="cart"),
    path("deletecart/<int:pk>",views.deletecart,name='deletecart'),
    path("details/<int:pk>",views.details,name="details"),
]
"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path
from page import views
from orders import views as orderviews
from contact.views import ContactView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'), 
    path('order/', views.order,name='order'), 
    path('contact/', ContactView.as_view(),name="contact"),
    path('pizza/', views.pizza,name='pizza'),
    path('hamburger/', views.hamburger,name='hamburger'),
    path('cold_drinks/', views.drink,name='drink'),
    path('teas/', views.tea,name='tea'),
    path('coffees/', views.coffee,name='coffee'),
    path('desserts/', views.dessert,name='dessert'), 
    path('order/', views.order , name='order'),
    path('order/create', orderviews.createOrder,name='createOrder'), 
]

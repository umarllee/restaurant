from django.shortcuts import render
from django.core.mail import send_mail
from restaurant import settings
def index(request): 
    return  render(request,'index.html')

def order(request):
    return render(request, 'Online_Order.html')
 
def contact(request):
    return render(request, 'Contact.html')
 
def pizza(request):
    return render(request,'Pizzas.html')
 
def hamburger(request):
    return render(request,'Hamburgers.html')

def drink(request):
    return render(request,'Cold_Drinks.html')

def tea(request):
    return render(request,'Teas.html')

def coffee(request):
    return render(request,'Coffees.html')

def dessert(request):
    return render(request,'Desserts.html')
 
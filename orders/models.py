from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime, date


class Order(models.Model):
    namelastname= models.CharField(max_length=100,verbose_name="Name and Lastname")
    address= models.CharField(max_length=100,verbose_name="Address")
    phone= models.CharField(max_length=100,verbose_name="Phone number")
    total_view= models.DecimalField(max_digits=10000,decimal_places=2,verbose_name="Amount")
   # billing_status= models.BooleanField(default=False,verbose_name="Paid")
    itemname = models.CharField(max_length=50, null=True,verbose_name="Item name")
    say = models.IntegerField(default=0, null=True, blank=True,verbose_name="How much")
    date = models.DateField(default=timezone.now)
    time=models.TimeField(auto_now=True, auto_now_add=False)


 
  
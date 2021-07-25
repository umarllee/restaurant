from django.contrib import admin
from . models import Order

@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display=('namelastname' , 'address' , 'phone' , 'total_view' , 'itemname' , 'say', 'date', 'time')
 
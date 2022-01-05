from django.contrib import admin
from delivery.models import Customer, Deliveryman, Food, Restaurant, Orderform
# Register your models here.

admin.site.register([Customer, Deliveryman, Food, Restaurant, Orderform])

from django.contrib import admin


# Register your models here.
from .models import Topping,Pizza,Drink

admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Drink)


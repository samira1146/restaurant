from django.db import models
from django.contrib.auth.models import User


# Create your models



class Topping(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name



class Pizza(models.Model):
    name=models.CharField(max_length=15)
    size = models.CharField(max_length=10)
    price= models.FloatField()
    topping = models.ManyToManyField(Topping)

    class Meta:
        ordering = ['name']

    def __str__(self):
        template = '{0.name} {0.size}'
        return template.format(self)




class Drink(models.Model):
    name = models.CharField(max_length=15)
    size= models.CharField(max_length=10)
    type=models.CharField(max_length=10)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name,self.size,self.type



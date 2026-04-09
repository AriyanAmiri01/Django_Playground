from django.db import models



# Create your models here
class Client(models.Model): # defining  a new model
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    password = models.CharField( max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Admin(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length =50)
    email = models.EmailField( max_length=254)
    password = models.CharField( max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Writer(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length =50)
    email = models.EmailField( max_length=254)
    password = models.CharField( max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
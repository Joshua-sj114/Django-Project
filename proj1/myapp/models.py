from django.db import models

# Create your models here.
class User(models.Model): # This creates a 'User' table in the database # create table User()
    user_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID') 
    name = models.CharField(max_length = 255) # name, VARCHAR(255)
    age = models.BigIntegerField(null=True)

class Product(models.Model):
    product_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID') 
    product_name = models.CharField(max_length=80)
    product_description = models.TextField(max_length=255)
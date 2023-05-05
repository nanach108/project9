from django.db import models

# Create your models here.

class Computers(models.Model):
    item=models.CharField(max_length=50,null=True,blank=True)
    ram = models.CharField(max_length=256,null=True,blank=True)
    storage = models.CharField(max_length=256,null=True,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    # createdTime=models.DateTimeField(auto_now_add=True)
    fields =['item','ram','storage','price']
 
    def __str__(self):
           return self.item
    

class Phones(models.Model):
    item=models.CharField(max_length=50,null=True,blank=True)
    storage = models.CharField(max_length=256,null=True,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    fields =['item','ram','storage','price']
 
    def __str__(self):
           return self.item
    
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    complete_name = models.CharField(max_length=254)
    email=models.EmailField(default="email@example.com",max_length = 254)
    fields=["complete_name","email"]

    def __str__(self):
        return self.complete_name
    

class CustomerUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    complete_name = models.CharField(max_length=254)
    email=models.EmailField(default="email@example.com",max_length = 254)

    fields=["complete_name","email"]

    def __str__(self):
        return self.complete_name
    



from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=15, decimal_places=2)
    category=models.CharField(max_length=63)
    feature_image = models.ImageField(upload_to = 'products/', blank = True, null = True)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=255)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    
    def __str__(self):
        return self.name

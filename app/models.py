from django.db import models
# Create your models here.


# CATEGORY_CHOICES =(
#     ('M', 'Mobile'),
#     ('L','Laptop'),
#     ('TW','Top Wear'),
#     ('BW', 'Bottom Wear'),
# )    

# class Product(models.Model):
#     title = models.CharField(max_length=100)
#     selling_price=models.FloatField()
#     discounted_price=models.FloatField()
#     description=models.TextField()
#     brand = models.CharField(max_length=200)
#     category = models.CharField(choices = CATEGORY_CHOICES,max_length=2)
#     product_image = models.ImageField(upload_to='producting')
    
#     def __str__(self):
#         return str(self.id)
    
CATEGORY_CHOICE = (
    ("MOBILE","MOBILE"),
    ("LAPTOP","LAPTOP"),
    ("TOPWERE","TOPWERE"),
    ("BOTTOMWERE","BOTTOMWERE"),
    ("ELECTRONIC","ELECTRONIC"),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    decription = models.TextField()
    brand = models.CharField(max_length=200)
    category = models.CharField(max_length=10,choices=CATEGORY_CHOICE)
    Product_image =models.ImageField(upload_to="producting/")
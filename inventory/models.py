from django.db import models


class Category(models.Model):
    name  = models.CharField(max_length=255,blank=True,null=True)

class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')
class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField(blank=True,null=True)
    stock = models.IntegerField(blank=True,null=True)
    
class ProductReview(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    review = models.TextField(blank=True,null=True)
    rating = models.IntegerField(blank=True,null=True)
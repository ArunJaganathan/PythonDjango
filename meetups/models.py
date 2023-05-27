from django.db import models

# Create your models here.
class Latestorder(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,null=True)
    orderId=models.CharField(max_length=200)
    description=models.TextField()
    popularity = models.IntegerField(blank=True,null=True)
    STATUS_OBJ = (
        ('1', 'Shipped'),
        ('2', 'Pending'),
        ('3', 'Delivered'),
        ('4', 'Processing'),
    )
    status = models.CharField(max_length=2, choices=STATUS_OBJ,blank=True,null=True)




class Recentlyaddedproducts(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,null=True)
    description=models.TextField()
    rate = models.IntegerField(blank=True,null=True)      
    STATUS_OBJ = (
        ('1', 'Active'),
        ('2', 'In Active'),
        ('3', 'Draft'),
    ) 
    #image = models.ImageField(upload_to='product/images/')   
    status = models.CharField(max_length=2, choices=STATUS_OBJ,blank=True,null=True) 
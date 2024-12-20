from django.db import models

# Create your models here.

class Featured_Products(models.Model):
    image= models.ImageField(upload_to= "featured_products", blank=True)
    
    product_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name_plural = "Featured Products"
        
class Latest_Products(models.Model):
    image= models.ImageField(upload_to="latest_products",blank=False)
    
    product_name= models.CharField(max_length=100)
    
    price= models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def __str__(self):
     return self.product_name
 
    class Meta:
        verbose_name_plural = "Latest Products"
        
class Newsletter(models.Model):
    email= models.EmailField(max_length=200)
    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = "Newsletter"

class Slider(models.Model):
    image= models.ImageField(upload_to="slider", blank=False)
    title= models.CharField(max_length=100)
    description= models.TextField(max_length=250, blank=True)   
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Slider"
        
class Product_Listing(models.Model):
    image= models.ImageField(upload_to="product_listing",blank=False)
    
    name_of_product = models.CharField(max_length=100)
    
    price= models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def __str__(self):
     return self.name_of_product
 
    class Meta:
        verbose_name_plural = "Product Listings"

    
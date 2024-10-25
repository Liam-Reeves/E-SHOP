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
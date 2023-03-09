from django.db import models
from products.models import Product

class Category(models.Model):

    dia = models.CharField(max_length=50)
    description = models.TextField()
    products = models.ManyToManyField(Product, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        
        return self.dia
    

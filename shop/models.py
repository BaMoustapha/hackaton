from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to="products/%Y/%m%d")
    description = models.TextField(blank=True)
    
    
    def __str__(self):
        return self.name
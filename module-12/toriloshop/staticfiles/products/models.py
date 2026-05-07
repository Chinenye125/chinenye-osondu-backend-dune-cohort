from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default= 0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE,
        related_name = 'products'
    )

    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    is_available = models.BooleanField(default=True)
    stock = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(1)])
    image= models.ImageField(upload_to='images/', null=True, blank=True)
    is_hidden = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, related_name='products', blank=True)



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Optionnel, pour lier à un utilisateur
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} "

class ItemOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Order: {self.order.id}"

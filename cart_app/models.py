
from django.db import models
from app.models import Clothes
from django.contrib.auth.models import User

class CartItem(models.Model):
    product = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    def get_total_price(self):
        return self.quantity * self.product.price

    def save(self, *args, **kwargs):
        if self.quantity < 1:
            raise ValueError("Quantity must be at least 1")
        super().save(*args, **kwargs)

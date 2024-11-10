
#  for differentiating between male and female clothes
from django.db import models

class Clothes (models.Model):
    GENDER_CHOICES = [
        ('male', 'Male Wear'),
        ('female', 'Female Wear'),
    ]
    
    ITEM_CATEGORY_CHOICES = [
        ('shirt', 'Shirt'),
        ('pants', 'Pants'),
        ('dress', 'Dress'),
        ('accessory', 'Accessory'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    gender_category = models.CharField(max_length=6, choices=GENDER_CHOICES)
    item_category = models.CharField(max_length=20, choices=ITEM_CATEGORY_CHOICES)
    image = models.ImageField(upload_to='clothes_images/')

    def __str__(self):
        return f"{self.name} - {self.get_gender_category_display()}"










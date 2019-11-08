import os
from django.db import models

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Cake(models.Model):
    cake_ID = models.AutoField(primary_key=True)
    cake_name = models.CharField(max_length=100)
    date_made = models.DateField(auto_now=True)
    descr = models.TextField(blank=True)
    cake_customer = models.CharField(max_length=100)
    cake_picture = models.ImageField(upload_to=get_image_path, height_field=None, width_field=None, max_length=None, blank=True, null=True)
    def __str__(self):
        return self.cake_name 

class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=200)
    price_paid = models.DecimalField(max_digits=5, decimal_places=2)
    price_gram = models.DecimalField(max_digits=5, decimal_places=5)
    def __str__(self):
        return self.ingredient_name

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    cake_id = models.ForeignKey("Cake", on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    user_comment = models.TextField(blank=True)
    rating = models.IntegerField(default=5)
    def __str__(self):
        return self.user
    
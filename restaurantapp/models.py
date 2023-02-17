from django.db import models
from django.urls import reverse

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=100, unique=True)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return f'title={self.title}; price={self.price}'
    
    def get_absolute_url(self):
        return reverse('menu')
    
    def available(self):
        return all(i.enough() for i in self.reciperequirement_set.all())

class Ingredient(models.Model):
    name = models.CharField(max_length=30, unique=True)
    qty = models.FloatField(default=0.0)
    unit = models.CharField(max_length=10)
    unit_price = models.FloatField(default=0.0)

    def get_absolute_url(self):
        return reverse('ingredient')

    def __str__(self):
        return f"""
        name={self.name}; 
        qty={self.qty};
        unit={self.unit}; 
        unit_price={self.unit_price}"""

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    qty = models.FloatField(default=0)

    def __str__(self):
        return f"""
        menu_item=[{self.menu_item.__str__()}]; 
        ingredient={self.ingredient.name}; 
        qty={self.qty}"""

    def get_absolute_url(self):
        return reverse('menu')

    def enough(self):
        return self.qty <= self.ingredient.qty

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; time={self.timestamp}"
    
    def get_absolute_url(self):
        return reverse('purchase')

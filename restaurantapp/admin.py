from django.contrib import admin
from .models import MenuItem, Ingredient, Purchase, RecipeRequirement

# Register your models here.
[admin.site.register(i) for i in [MenuItem, Ingredient, Purchase, RecipeRequirement]]
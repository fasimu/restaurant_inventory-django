from django.forms import ModelForm
from .models import *

class AddForm(ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class RecipeRequirementForm(ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"

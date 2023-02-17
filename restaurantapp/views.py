from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.db.models import Sum, F
from django.shortcuts import redirect, render

from .models import *
from .forms import *

# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'restaurantapp/home.html'
    
    def get(self, request):
        return render(request, self.template_name)

class MenuListView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = 'restaurantapp/menu.html'

class NewMenuListView(LoginRequiredMixin, CreateView):
    template_name = "restaurantapp/add_menu.html"
    model = MenuItem
    form_class = AddForm

class DeleteMenuListView(LoginRequiredMixin, DeleteView):
    template_name = "restaurantapp/delete_menu.html"
    model = MenuItem
    success_url = '/menu'

class IngredientView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = 'restaurantapp/ingredient.html'

class NewIngredientView(LoginRequiredMixin, CreateView):
    template_name = "restaurantapp/add_ingredient.html"
    model = Ingredient
    form_class = IngredientForm

class UpdateIngredientView(LoginRequiredMixin, UpdateView):
    template_name = "restaurantapp/update_ingredient.html"
    model = Ingredient
    form_class = IngredientForm

class NewRecipeRequirementView(LoginRequiredMixin, CreateView):
    template_name = 'restaurantapp/add_recipereq.html'
    model = RecipeRequirement
    form_class = RecipeRequirementForm

class PurchaseView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = 'restaurantapp/purchase.html'

class NewPurchaseView(LoginRequiredMixin, TemplateView):
    template_name = 'restaurantapp/add_purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = [i for i in MenuItem.objects.all()] #if i.available()
        return context 
    
    def post(self, request):
        menu_id = request.POST['menu_item']
        menu_item = MenuItem.objects.get(pk=menu_id)
        requirements = menu_item.reciperequirement_set
        purchase = Purchase(menu_item=menu_item)
        for req in requirements.all():
            req_ingredient = req.ingredient
            req_ingredient.qty -= req.qty
            req_ingredient.save()
        purchase.save()
        return redirect('purchase')

class ReportView(LoginRequiredMixin, TemplateView):
    template_name = "restaurantapp/report.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(
            revenue=Sum("menu_item__price"))["revenue"]
        total_cost = 0
        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
                total_cost += recipe_requirement.ingredient.unit_price * recipe_requirement.qty

        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost

        return context

def log_out(request):
    logout(request)
    return redirect("/")
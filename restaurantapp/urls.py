from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path("logout/", log_out, name="logout"),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path('', HomeView.as_view(), name='home'),
    path('menu/', MenuListView.as_view(), name='menu'),
    path('menu/new', NewMenuListView.as_view(), name='add_menu'),
    path('delete_menu/<slug:pk>/delete', DeleteMenuListView.as_view(), name='delete_menu'),
    path('ingredient/', IngredientView.as_view(), name='ingredient'),
    path('ingredient/new', NewIngredientView.as_view(), name='add_ingredient'),
    path('ingredient/<slug:pk>/update', UpdateIngredientView.as_view(), name='update_ingredient'),
    path('reciperequirement/new', NewRecipeRequirementView.as_view(), name='add_recipereq'),
    path('purchase/', PurchaseView.as_view(), name='purchase'),
    path('purchase/new', NewPurchaseView.as_view(), name='add_purchase'),
    path('report', ReportView.as_view(), name='report'),
    ]
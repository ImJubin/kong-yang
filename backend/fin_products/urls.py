from django.urls import path
from . import views

app_name="products"
urlpatterns = [
    path('deposits/', views.deposit_products_view, name='deposits'),
    path('savings/', views.savings_products_view, name='savings'),
]

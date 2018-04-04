from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<str:category_slug>', product_list, name='product_list_by_category'),

]
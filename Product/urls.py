from django.urls import path
from Product.views import product_list,product_create, product, product_slug
urlpatterns=[
    path('list/',product_list),
    path('',product_create),
    path('<int:pk>',product),
    path('<str:slug>',product_slug),
]
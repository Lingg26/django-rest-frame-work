from django.urls import path
from CategoryItems.views import cateitem_list,cateitem_create, categoryitem, categoryitem_slug
urlpatterns=[
    path('list/',cateitem_list),
    path('',cateitem_create),
    path('<int:pk>',categoryitem),
    path('<str:slug>', categoryitem_slug)
    # path('<str:slug>',product_list_cateitem)
]
from django.urls import path
from CheckOut.views import checkout_list,checkout_create, checkout_tourcode
urlpatterns=[
    path('list/',checkout_list),
    path('',checkout_create),
    path('<str:tour_code>', checkout_tourcode),
]
from django.urls import path
from TourCodes.views import tourcode_list,tourcode_create, tourCode, tourcode_tc
urlpatterns=[
    path('list/',tourcode_list),
    path('',tourcode_create),
    path('<int:pk>',tourCode),
    path('<str:tour_code>', tourcode_tc),
]
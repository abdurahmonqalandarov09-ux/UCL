from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main)
]

urlpatterns = [
    path('results/', results)
]

urlpatterns = [
    path('standings/', standing)
]
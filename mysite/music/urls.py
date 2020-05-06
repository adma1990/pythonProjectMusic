from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('band/<int:id>', band_list, name='band_list')


]
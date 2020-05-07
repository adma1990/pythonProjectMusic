from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('band_list/<int:id>', band_list, name='band_list'),
    path('band_main/<int:id>', band_main, name='band_main'),
    path('album/<int:id>', album, name='album'),


]
from django.contrib import admin
from .models import GenreMusic, Band, Album, Images
# Register your models here.

admin.site.register(GenreMusic)
admin.site.register(Band)
admin.site.register(Album)
admin.site.register(Images)

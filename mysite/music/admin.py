from django.contrib import admin
from .models import GenreMusic, Band, Album, Images, ImagesAlbum
# Register your models here.

admin.site.register(GenreMusic)
admin.site.register(Band)
admin.site.register(Album)
admin.site.register(Images)
admin.site.register(ImagesAlbum)

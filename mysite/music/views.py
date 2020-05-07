from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    genre_music = GenreMusic.objects.all()#список стилей
    image_home_page = Images.objects.all()
    contex = {
        "genre_music" : genre_music,
        'image_home_page':image_home_page
    }
    return render(request, 'music/home.html', contex)

def band_list(request, id):
    genre_music = GenreMusic.objects.all()
    band_list = Band.objects.get(id=id)
    list = Band.objects.filter(genre__id=id)#получаем список каждой группы согласно ее жанру
    context = {
        'band_list':band_list,
        'list':list,
        'genre_music':genre_music

    }
    return render(request, 'music/band_list.html', context)

def band_main(request, id):
    genre_music = GenreMusic.objects.all()
    albums = Album.objects.filter(band__id=id)#получаем список альбомов согласно конкретной группе
    context = {
        'albums':albums,
        'genre_music': genre_music
    }
    return render(request, 'music/band_main.html', context)

def album(request, id):
    genre_music = GenreMusic.objects.all()
    image_album = ImagesAlbum.objects.filter(album__id=id)#получаем изображение обложек альбомов
    context = {
        'image_album':image_album,
        'genre_music': genre_music
    }
    return render(request, 'music/album.html', context)
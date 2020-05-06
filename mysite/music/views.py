from django.shortcuts import render
from .models import GenreMusic, Band, Album, Images

# Create your views here.
def home(request):
    genre_music = GenreMusic.objects.all()
    contex = {"genre_music" : genre_music}
    return render(request, 'music/home.html', contex)

def band_list(request, id):
    band_list = Band.objects.get(id=id)
    list = Band.objects.filter(genre__id=id).all()
    image = Images.objects.get(id=id)
    context = {
        'band_list':band_list,
        'image':image,
        'list':list,

    }
    return render(request, 'music/band_list.html', context)

def band_main(request, id):
    band = Band.objects.get(id=id)
    image = Images.objects.get(id=id)
    context = {
        'band':band,
        'image':image
    }
    return render(request, 'music/band_main.html', context)


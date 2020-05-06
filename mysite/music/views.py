from django.shortcuts import render
from .models import GenreMusic, Band, Album, Images

# Create your views here.
def home(request):
    genre_music = GenreMusic.objects.all()
    contex = {"genre_music" : genre_music}
    return render(request, 'music/home.html', contex)

def band_list(request, id):
    band_list = Band.objects.get(id=id)
    context = {'band_list':band_list}
    return render(request, 'music/band_list.html', context)


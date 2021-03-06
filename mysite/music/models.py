from django.db import models

# Create your models here.

#модель отвечает за список жанров
class GenreMusic(models.Model):
    name_genre = models.CharField(max_length=70)

    class Meta():
        verbose_name = "Жанры"

    def __str__(self):
        return self.name_genre

#модель отвечает за музыкальные группы и связана с моделью GenreMusic
class Band(models.Model):
    name_band = models.CharField(max_length=100)
    year_create = models.CharField(max_length=15)
    members = models.TextField()
    former_members = models.TextField()
    genre = models.ForeignKey(GenreMusic, on_delete=models.CASCADE)

    class Meta():
        verbose_name = "Группы"

    def __str__(self):
        return self.name_band

#модель отвечает за альбомы групп связана с моделью Band
class Album(models.Model):
    name_album = models.CharField(max_length=70)
    year_release = models.CharField(max_length=15)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    class Meta():
        verbose_name = "Альбомы"

    def __str__(self):
        return self.name_album

#модель отвечает за изображения альбомов
#связана с Album
class ImagesAlbum(models.Model):
    image_album = models.ImageField(upload_to='images')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    class Meta():
        verbose_name = "Изображения обложек альбомов"

#модель для всех остальных изображений
class Images(models.Model):
    imageAll = models.ImageField(upload_to='images')

    class Meta():
        verbose_name = "Изображения"








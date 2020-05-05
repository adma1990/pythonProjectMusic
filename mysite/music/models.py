from django.db import models

# Create your models here.

class GenreMusic(models.Model):
    name_genre = models.CharField(max_length=70)

    class Meta():
        verbose_name = "Жанры"

    def __str__(self):
        return self.name_genre

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

class Album(models.Model):
    name_album = models.CharField(max_length=70)
    year_release = models.CharField(max_length=15)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    class Meta():
        verbose_name = "Альбомы"

    def __str__(self):
        return self.name_album

class Images(models.Model):
    image = models.ImageField(upload_to='images')
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    class Meta():
        verbose_name = "Изображения"







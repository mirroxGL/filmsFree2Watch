from django.db import models

class Film(models.Model):
    title = models.CharField("Title", max_length=50)
    rating = models.CharField("Rating", max_length=3)
    description = models.TextField("Description", max_length=250, default='')
    director = models.CharField("Director", max_length=30, default='')
    image_url = models.TextField("Image", max_length=250)
    imdb_url = models.TextField("Imdb", max_length=250)
    rezka_url = models.TextField("Hdrezka", max_length=250)

    def get_absolute_url(self):
        return f"/{self.id}"

    def __str__(self):
        return self.title



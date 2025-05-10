from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    tekst = models.TextField(max_length=250, null=True, blank=True)
    teksteind = models.TextField(max_length=250, null=True, blank=True)
    kollom = models.CharField(max_length=5, null=True, blank=True)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)
    #afbeelding = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.title

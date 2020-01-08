from django.db import models
from django.utils.text import slugify
from time import time
from django.shortcuts import reverse

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug

class Show(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    summary = models.TextField()
    thumb = models.ImageField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('show_detail_url', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

class Season(models.Model):
    number = models.IntegerField()
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    def __str__(self):
        return self.show.title + '/' + str(self.number)

class Episode(models.Model):
    number = models.IntegerField()
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    file = models.FileField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return self.season.show.title + '/s' + str(self.season.number) + '/' + str(self.number)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug=slugify(self.season.show.title +'-s'+str(self.season.number)+'-'+str(self.number))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('episode_detail_url', kwargs={'slug':self.slug})

class Genre(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    shows = models.ManyToManyField('Show', blank=True, related_name='genres')

    def get_absolute_url(self):
        return reverse('genre_related_shows_url', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

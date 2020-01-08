from django.contrib import admin
from .models import *


admin.site.register([Show, Genre])

class EpisodeInline(admin.StackedInline):
    model = Episode

class SeasonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name of the show: ', {'fields':['show']}),
        ('Number of season: ', {'fields':['number']}),

    ]
    inlines = [EpisodeInline]

admin.site.register(Season, SeasonAdmin)

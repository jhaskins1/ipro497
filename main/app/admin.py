from django.contrib import admin
from .models import Movie, Genre, Cast, Language, StreamingOption
# Register your models here.

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Cast)
admin.site.register(Language)
admin.site.register(StreamingOption)
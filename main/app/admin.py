from django.contrib import admin
from .models import Movie, Genre, Cast, Language, StreamingOption
# Register your models here.

# Once you create the models and migrate the model specifications to the database, you will need to register
# the model into the admin interface for verification and total control. Admin section is something that we won't
# use, but it will serve as verification that data is being recorded into the database.


admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Cast)
admin.site.register(Language)
admin.site.register(StreamingOption)
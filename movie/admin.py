from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Movies
# Register your models here.
@admin.register(Movies)
class MovieName(ImportExportModelAdmin):
    pass
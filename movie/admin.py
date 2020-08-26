from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Movies,Profile
# Register your models here.
admin.site.register(Profile)
@admin.register(Movies)
class MovieName(ImportExportModelAdmin):
    pass
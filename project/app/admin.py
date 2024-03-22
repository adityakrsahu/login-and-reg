from django.contrib import admin
from .models import DataStore

# Register your models here.
# admin.site.register(DataStore)

@admin.register(DataStore)
class DataStoreAdmin(admin.ModelAdmin):
    list_display =['id','First_Name','Qualification']


from django.contrib import admin
from .models import *
# Register your models here.
class about_infoAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' ,'img' , 'des']
admin.site.register(about_info, about_infoAdmin)
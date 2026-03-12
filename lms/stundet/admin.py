from django.contrib import admin
from .models import *
# Register your models here.
class about_infoAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' ,'img' , 'des']
admin.site.register(about_info, about_infoAdmin)

class contact_infoAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'email' , 'subject' , 'message']
admin.site.register(contact_info , contact_infoAdmin)

class RegisteredUserAdmin(admin.ModelAdmin):
    list_display = ['id' , 'first_name' , 'last_name' , 'email' , 'city' , 'password' , 'phone' , 'course' , 'zip_code' , 'country']
admin.site.register(RegisteredUser , RegisteredUserAdmin)
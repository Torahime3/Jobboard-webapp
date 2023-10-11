from django.contrib import admin

# Register your models here.
from .models import Login

class LoginAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'email')

admin.site.register(Login,LoginAdmin)

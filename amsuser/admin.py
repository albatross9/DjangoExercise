from django.contrib import admin
from .models import Amsuser

# Register your models here.


class AmsAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(Amsuser, AmsAdmin)

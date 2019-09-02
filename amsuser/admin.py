from django.contrib import admin
from .models import Amsuser

# Register your models here.


class AmsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Amsuser, AmsAdmin)

from django.contrib import admin
from .models import *

# Register your models here.
class VagasAdmin(admin.ModelAdmin):
    list_filter = ['empresa']    

admin.site.register(Vaga_Emprego, VagasAdmin)
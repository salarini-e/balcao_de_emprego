from django.contrib import admin
from .models import *

# Register your models here.
class VagasAdmin(admin.ModelAdmin):
    list_filter = ['empresa']    

admin.site.register(Vaga_Emprego, VagasAdmin)
admin.site.register(Empresa)
admin.site.register(Escolaridade)
admin.site.register(Vaga)
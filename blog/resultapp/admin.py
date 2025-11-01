from django.contrib import admin
from .models import Skills,Vacancies,Requirements
# Register your models here.

admin.site.register(Skills)
admin.site.register(Requirements)
admin.site.register(Vacancies)

def set_active(queryset):
    queryset.update(is_active=True)

from django.contrib import admin
from .models import Whore


class WhoreAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('name', 'venereal', 'birth_year', 'boobs', 'feature',)
    # Добавляем интерфейс для поиска по имени
    search_fields = ('name', 'venereal',)
    # Добавляем возможность фильтрации по имени
    list_filter = ('name',)


admin.site.register(Whore, WhoreAdmin)

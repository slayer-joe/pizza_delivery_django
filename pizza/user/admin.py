from django.contrib import admin
from user.models import User

class AdminUser(admin.ModelAdmin):
    list_display = ("username", "is_staff", "is_superuser")# отображаемые свойства в админке ,берем из таблицы users базы данных

admin.site.register(User, AdminUser)

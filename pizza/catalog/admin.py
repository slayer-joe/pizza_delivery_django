from django.contrib import admin
from .models import PizzaModel, Category

admin.site.register(PizzaModel)
admin.site.register(Category)
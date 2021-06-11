from django.contrib import admin
from .models import Dish, Ingredient, DayOfWeek, MenuForWeek


admin.site.register(Dish)
admin.site.register(Ingredient)
admin.site.register(DayOfWeek)
admin.site.register(MenuForWeek)

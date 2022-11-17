from django.contrib import admin
from .models import Measurement, Ingredient, Image, Recipe, Recipe_Ingredient
# Register your models here.
admin.site.register(Measurement)
admin.site.register(Ingredient)
admin.site.register(Image)
admin.site.register(Recipe)
admin.site.register(Recipe_Ingredient)

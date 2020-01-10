from django.contrib import admin

from recipes.models import IngredientCategory, Ingredient

admin.site.register(IngredientCategory)
admin.site.register(Ingredient)

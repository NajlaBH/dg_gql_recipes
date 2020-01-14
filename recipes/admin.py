from django.contrib import admin

from recipes.models import IngredientCategory, Ingredient, Recipe

admin.site.register(IngredientCategory)
admin.site.register(Ingredient)
admin.site.register(Recipe)

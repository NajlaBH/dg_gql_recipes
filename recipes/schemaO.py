# dg_gql_recipes/recipes/schema.py
# About = Recipes GraphQL schema Jan20/version-1.0.0
# Modified by = BY NajlaBH Jan20/version-1.0.1

import graphene

from graphene_django.types import DjangoObjectType

from recipes.models import IngredientCategory, Ingredient


class IngredientCategoryType(DjangoObjectType):
    class Meta:
        model = IngredientCategory


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient

class Query(object):
    all_categories = graphene.List(IngredientCategoryType)
    all_ingredients = graphene.List(IngredientType)

    def resolve_all_categories(self, info, **kwargs):
        return IngredientCategory.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related('category').all()

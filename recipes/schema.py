# dg_gql_recipes/recipes/schema.py
# About = Recipes GraphQL schema Jan20/version-1.0.0
# Modified by = BY NajlaBH Jan20/version-1.0.1

import graphene

from graphene_django.types import DjangoObjectType

from recipes.models import IngredientCategory, Ingredient

from recipes.types import IngredientCategoryType, IngredientType


class Query(object):
    """
    Class for Queries creation :
    query1 -  all categories
    query2 -  all ingredients
    query3 -  by categry

    """

    category = graphene.Field(IngredientCategoryType,
                        id=graphene.Int(),
                        name=graphene.String())
    all_categories = graphene.List(IngredientCategoryType)

    ingredient = graphene.Field(IngredientType,
                            id=graphene.Int(),
                            name=graphene.String())
    all_ingredients = graphene.List(IngredientType)

    def resolve_all_categories(self, info, **kwargs):
        return IngredientCategory.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related('category').all()
    
    def resolve_category(self, info, **kwargs):
          id = kwargs.get('id')
          name = kwargs.get('name')

          if id is not None:
              return IngredientCategory.objects.get(pk=id)

          if name is not None:
              return IngredientCategory.objects.get(name=name)

          return None

    def resolve_ingredient(self, info, **kwargs):
          id = kwargs.get('id')
          name = kwargs.get('name')

          if id is not None:
              return Ingredient.objects.get(pk=id)

          if name is not None:
              return Ingredient.objects.get(name=name)

          return None


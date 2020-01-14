# dg_gql_recipes/recipes/types.py
# About = Recipes GraphQL schema Jan20/version-1.0.0
# Modified by = BY NajlaBH Jan20/version-1.0.1

import graphene

from graphene_django.types import DjangoObjectType

from recipes.models import IngredientCategory, Ingredient


# Create Django Object Types
class IngredientCategoryType(DjangoObjectType):
    class Meta:
        model = IngredientCategory


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient


# Create Graphen Input Object Types
class IngredientCategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

class IngredientInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    notes = graphene.String()
    category = graphene.String()

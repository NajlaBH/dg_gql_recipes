# dg_gql_recipes/recipes/types.py
# About = Recipes GraphQL schema Jan20/version-1.0.0
# Modified by = BY NajlaBH Jan20/version-1.0.1

import graphene

from graphene_django.types import DjangoObjectType

from recipes.models import IngredientCategory, Ingredient, Recipe


# Create Django Object Types
# Create a GraphQL type for the IngredientCategory model
class IngredientCategoryType(DjangoObjectType):
    class Meta:
        model = IngredientCategory

# Create a GraphQL type for the Ingredient model
class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient

# Create a GraphQL type for the recipe model
class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe

# Create Graphen Input Object Types
class IngredientCategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

class IngredientInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    notes = graphene.String()
    category = graphene.String()

class RecipeInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    ingredients = graphene.List(IngredientInput)
    description = graphene.String()
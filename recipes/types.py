# dg_gql_recipes/recipes/types.py
# About = Recipes GraphQL schema Jan20/version-1.0.0
# Modified by = BY NajlaBH Jan20/version-1.0.1

import django_filters 
import graphene

from graphene_django.types import DjangoObjectType
from graphene import ObjectType, Connection, Node, Int
from graphene import relay

from recipes.models import IngredientCategory, Ingredient, Recipe
from recipes.models import IngredientCategory, Ingredient, Recipe



# Create Django Object Types
# Create a GraphQL type for the IngredientCategory model
class IngredientCategoryType(DjangoObjectType):
    """
    IngredientCategoryType: DjangoObjectType
    model
    """
    class Meta:
        model = IngredientCategory

# Create a GraphQL type for the Ingredient model
class IngredientType(DjangoObjectType):
    """
    IngredientType: DjangoObjectType
    model
    """
    class Meta:
        model = Ingredient


# Create a GraphQL type for the recipe model
class RecipeType(DjangoObjectType):
    """
    RecipeType: DjangoObjectType
    model
    """
    class Meta:
        model = Recipe

class IngredientNode(DjangoObjectType):
    """
    IngredientNode: DjangoObjectType
    model
    """
    class Meta:
        model = Ingredient
        filter_fields = {'id':['exact'],
                        'name':['exact', 'icontains', 'istartswith'],
                        'category': ['exact'],
                        'notes':['exact', 'icontains', 'istartswith'],}
        interfaces = (relay.Node, )


# Create Graphen Input Object Types
class IngredientCategoryInput(graphene.InputObjectType):
    """
    IngredientCategoryType: 
    params: id, name (wet, dry, fruit, ..)
    """
    id = graphene.ID()
    name = graphene.String()

class IngredientInput(graphene.InputObjectType):
    """
    IngredientInput: Category of ingredient such as (wet,dry,fruit ...)
    params: id,
    name(juice, milk, water, potatos,...)
    note (extracted from, cultivated as , ...)
    category: (fk: IngredientCategoryInput)
    """
    id = graphene.ID()
    name = graphene.String()
    notes = graphene.String()
    category = graphene.String()

class RecipeInput(graphene.InputObjectType):
    """
    RecipeInput: Category of recipe such as (breakfast, diner, pudding,...)
    params: id,
    name(juice, milk, water, potatos,...)
    note (extracted from, cultivated as , ...)
    category: (fk: IngredientCategoryInput)
    """
    id = graphene.ID()
    title = graphene.String()
    ingredients = graphene.List(IngredientInput)
    description = graphene.String()
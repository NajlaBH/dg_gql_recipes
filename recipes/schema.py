# dg_gql_recipes/recipes/schema.py
# About = Recipes GraphQL schema Jan20/version-1.0.0
# Modified by = BY NajlaBH Jan20/version-1.0.1

import graphene

from graphene_django.types import DjangoObjectType

from recipes.models import IngredientCategory, Ingredient, Recipe

from recipes.types import *


class Query(object):
    """
    Class for Queries creation :
    query1 -  all categories
    query2 -  all ingredients
    query3 -  by category

    """

    ingredientCategory = graphene.Field(IngredientCategoryType,
                        id=graphene.Int(),
                        name=graphene.String())

    category = graphene.Field(IngredientCategoryType,
                        id=graphene.Int(),
                        name=graphene.String())
    all_categories = graphene.List(IngredientCategoryType)

    ingredient = graphene.Field(IngredientType,
                            id=graphene.Int(),
                            name=graphene.String())
    all_ingredients = graphene.List(IngredientType)


    recipe = graphene.Field(RecipeType, id=graphene.Int())
    
    all_recipes = graphene.List(RecipeType)

    def resolve_all_categories(self, info, **kwargs):
        return IngredientCategory.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related('category').all()

    def resolve_all_recipes(self, info, **kwargs):
        return Recipe.objects.all()

    def resolve_ingredientCategory(self, info, **kwargs):
          id = kwargs.get('id')
          name = kwargs.get('name')

          if id is not None:
              return IngredientCategory.objects.get(pk=id)

          if name is not None:
              return IngredientCategory.objects.get(name=name)

          return None

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

    
    def resolve_recipe(self, info, **kwargs):
          id = kwargs.get('id')
          title = kwargs.get('title')

          if id is not None:
              return Recipe.objects.get(pk=id)

          if title is not None:
              return Recipe.objects.get(title=title)

          return None
    

# Create mutations for ingredientCategory
class CreateIngredientcategory(graphene.Mutation):
    """
    Create Ingredient category from mutation
    """
    class Arguments:
        input = IngredientCategoryInput(required=True)

    ok = graphene.Boolean()
    ingredientCategory = graphene.Field(IngredientCategoryType)

    def mutate(root, info, input=None):
        igc = IngredientCategory(name=input.name)
        ok = True
        igc.save()
        return CreateIngredientcategory(ingredientCategory=igc, ok=ok)

class UpdateIngredientcategory(graphene.Mutation):
    """
    Update Ingredient category from mutation
    """
    class Arguments:
        id = graphene.Int(required=True)
        input = IngredientCategoryInput(required=True)

    ok = graphene.Boolean()
    ingredientCategory = graphene.Field(IngredientCategoryType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        igc = IngredientCategory.objects.get(pk=id)
        if igc:
            ok = True
            igc.name = input.name
            igc.save()
            return UpdateIngredientcategory(ok=ok, ingredientCategory=igc)
        return UpdateIngredientcategory(ok=ok, ingredientCategory=None)  


# Create mutations for Ingredient
class CreateIngredient(graphene.Mutation):
    """
    Create Ingredient  from mutation
    """
    class Arguments:
        name= graphene.String()
        notes = graphene.String()
        category_id= graphene.Int()

    ok = graphene.Boolean()
    ingredient = graphene.Field(IngredientType)
    category= graphene.Field(IngredientCategoryType)

    def mutate(root, info,name, notes, category_id):
        category=IngredientCategory.objects.get(id=category_id)
        igi = Ingredient(name=name, notes=notes, category=category)
        ok = True
        igi.save()
        return CreateIngredient(ingredient=igi, ok=ok)


class UpdateIngredient(graphene.Mutation):
    """
    Update Ingredient  from mutation
    """
    class Arguments:
        id = graphene.Int(required=True)
        name= graphene.Argument(graphene.String)
        notes = graphene.String()
        category_id= graphene.Int()


    ok = graphene.Boolean()
    ingredient = graphene.Field(IngredientType)
    category= graphene.Field(IngredientCategoryType)

    @staticmethod
    def mutate(root, info, id, name, notes, category_id):
        ok = False
        igi = Ingredient.objects.get(pk=id)
        if igi:
            ok = True
            category=IngredientCategory.objects.get(id=category_id)
            igi.name = name
            igi.notes = notes
            igi.category = category
            igi.save()
            return UpdateIngredient(ok=ok, ingredient=igi)
        return UpdateIngredient(ok=ok, ingredient=None) 


# Create mutations for recipes
class CreateRecipe(graphene.Mutation):
    class Arguments:
        input = RecipeInput(required=True)

    ok = graphene.Boolean()
    recipe = graphene.Field(RecipeType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        ingredients = []
        for ingredient_input in input.ingredients:
          ingredient = Ingredient.objects.get(pk=ingredient_input.id)
          if ingredient is None:
            return CreateRecipe(ok=False, recipe=None)
          ingredients.append(ingredient)
        ingredient_instance = Recipe(
          title=input.title,
          description=input.description
          )
        ingredient_instance.save()
        ingredient_instance.ingredients.set(ingredients)
        return CreateRecipe(ok=ok, recipe=ingredient_instance)

class Mutation(graphene.ObjectType):
    """
    Class for mutations creation
    - Create an ingredientCategory
    - Update an ingredientCategory
    - Create an ingredient
    - Update an ingredient
    - Create recipe
    """
    create_ingredientCategory = CreateIngredientcategory.Field()
    update_ingredientCategory = UpdateIngredientcategory.Field()
    create_ingredient = CreateIngredient.Field()
    update_ingredient = UpdateIngredient.Field()
    create_recipe = CreateRecipe.Field()
    

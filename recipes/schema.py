# dg_gql_recipes/recipes/schema.py
# About = Recipes GraphQL schema Jan20/version-1.0.0
# Modified by = BY NajlaBH Jan20/version-1.0.1

import graphene

from graphene_django.types import DjangoObjectType
from graphene import ObjectType
from graphene_django.filter import DjangoFilterConnectionField

from recipes.models import IngredientCategory, Ingredient, Recipe
from recipes.types import *


class Query(ObjectType):
    """
    Class for Queries creation :
    query1 -  all categories
    query2 -  all ingredients
    query3 -  ingredient category by name
    query4 -  ingredient by category
    query5 -  ingredient by name
    query6 -  by recipe
    query7 -  all recipes
    
    query8 - Make filter :
        - to comment (L63,L64) if you want to test file queries_test
        - to uncomment  (L63,L64) if you want to test file queries_filter_test
    """

    #Query 1
    all_categories = graphene.List(IngredientCategoryType,
    description="Get All categories")

    #Query 2
    all_ingredients = graphene.List(IngredientType,description="Get the list of Ingredients")

    #Query 3
    ingredientCategory = graphene.Field(IngredientCategoryType,
                        id=graphene.Int(),
                        name=graphene.String(),
                        description="Get Ingredient Category by name")

    #Query 4
    category = graphene.Field(IngredientCategoryType,
                        id=graphene.Int(),
                        name=graphene.String(),
                        description="Get Category by name")

    #Query 5
    ingredient = graphene.Field(IngredientType,
                            id=graphene.Int(),
                            name=graphene.String(),
                            description="Get Ingredient by name")

    #Query 6                      
    recipe = graphene.Field(RecipeType, id=graphene.Int(), description="Get Recipe by title")
    
    #Query 7
    all_recipes = graphene.List(RecipeType, description="Get All Recipes")

    #Query 8 : filter to comment if you want the basic schema without filter :)
    ingredientFilter = relay.Node.Field(IngredientNode)
    all_ingredientFilter = DjangoFilterConnectionField(IngredientNode,description="Get All Filtered")

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


# Create mutations for recipes:: create
class CreateRecipe(graphene.Mutation):
    """
    Create Recipe from mutation
    """
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


# Create mutations for recipes:: update
class UpdateRecipe(graphene.Mutation):
    """
    Update Recipe from mutation
    """

    class Arguments:
        id = graphene.Int(required=True)
        input = RecipeInput(required=True)

    ok = graphene.Boolean()
    recipe = graphene.Field(RecipeType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        recipe_instance = Recipe.objects.get(pk=id)
        if recipe_instance:
            ok = True
            ingredients = []
            for ingred_input in input.ingredients:
              ingredient = Ingredient.objects.get(pk=ingred_input.id)
              if ingredient is None:
                return UpdateRecipe(ok=False, recipe=None)
              ingredients.append(ingredient)
            recipe_instance.title=input.title
            recipe_instance.description=input.description
            recipe_instance.save()
            recipe_instance.ingredients.set(ingredients)
            return UpdateRecipe(ok=ok, recipe=recipe_instance)
        return UpdateRecipe(ok=ok, recipe=None)


class Mutation(graphene.ObjectType):
    """
    Class for mutations creation
    - Create an ingredientCategory
    - Update an ingredientCategory
    - Create an ingredient
    - Update an ingredient
    - Create recipe
    - Update recipe
    """
    create_ingredientCategory = CreateIngredientcategory.Field()
    update_ingredientCategory = UpdateIngredientcategory.Field()
    create_ingredient = CreateIngredient.Field()
    update_ingredient = UpdateIngredient.Field()
    create_recipe = CreateRecipe.Field()
    update_recipe = UpdateRecipe.Field()
    

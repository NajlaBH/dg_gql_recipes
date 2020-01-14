from django.db import models

class IngredientUnit(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class RecipeCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class RecipePopularity(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class IngredientCategory(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        IngredientCategory, related_name='ingredients', on_delete=models.CASCADE)

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)
    #recipetag = models.ForeignKey(
    #    RecipeCategory, related_name='recipes', on_delete=models.CASCADE)
    #vote  = models.ForeignKey(
    #    RecipePopularity, related_name='recipes', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
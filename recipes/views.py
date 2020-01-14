# dg_gql_recipes/recipes/views.py
# About = Recipes GraphQL views (search) Jan20/version-1.0.0
# Modified by = BY NajlaBH Jan20/version-1.0.1


from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from dg_gql_recipes.schema import schema


class GraphQLPageView(View):

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        result = schema.execute(search)
        return JsonResponse(result.data, safe=False)

#from django.views.generic import TemplateView
#class GraphQLPageView(Template):
#    template_name = "graphiql.html"
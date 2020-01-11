from django.shortcuts import render

from django.views.generic import TemplateView

class GraphQLPageView(TemplateView):
    template_name = "graphiql.html"

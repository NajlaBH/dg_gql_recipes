from django.urls import path
from django.contrib import admin

from graphene_django.views import GraphQLView

from recipes.views import GraphQLPageView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', GraphQLView.as_view(graphiql=True)),
    path('graphiql', GraphQLPageView.as_view(), name='graphiql'),
]

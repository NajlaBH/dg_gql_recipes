# dg_gql_recipes/schema.py
# About = dg_gql_recipes GraphQL schema Jan20/version-1.0.0
# Modified by = BY NajlaBH Jan20/version-1.0.1

import graphene

import recipes.schema


class Query(recipes.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    pass

schema = graphene.Schema(query=Query)

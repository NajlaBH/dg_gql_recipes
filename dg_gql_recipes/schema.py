# dg_gql_recipes/schema.py
# About = dg_gql_recipes GraphQL schema Jan20/version-1.0.0
# Modified by = BY NajlaBH Jan20/version-1.0.1

import graphene

import recipes.schema

class Query(recipes.schema.Query, graphene.ObjectType):
    """
    An example of queries is available under tests/queries_test.txt
    """
    pass

class Mutation(recipes.schema.Mutation, graphene.ObjectType):
    """
    An example of mutations is available under tests/mutations_test.txt
    """
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

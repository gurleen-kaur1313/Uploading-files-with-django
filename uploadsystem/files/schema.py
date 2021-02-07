from graphql import GraphQLError
from django.db.models import Q
import os
import graphene
from files.models import Files

class MyFile(graphene.ObjectType):
    class Meta:
        model = Files

class Query(graphene.ObjectType):
    allFiles = graphene.List(MyFile)
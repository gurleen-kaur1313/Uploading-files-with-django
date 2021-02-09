from graphene_file_upload.scalars import Upload
import graphene
from graphene_django import DjangoObjectType
from files.models import Files
from datetime import datetime


class MyFile(DjangoObjectType):
    class Meta:
        model = Files


class Query(graphene.ObjectType):
    allFiles = graphene.List(MyFile)

    def resolve_allFiles(self, info):
        return Files.objects.all()


class UploadMutation(graphene.Mutation):
    class Arguments:
        file = Upload(required=True)

    success = graphene.Boolean()

    def mutate(self, info, file, **kwargs):
        # do something with your file
        add = Files.objects.create(file=file, created=datetime.now)
        add.save()
        return UploadMutation(success=True)


class Mutation(graphene.ObjectType):
    upload_file = UploadMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

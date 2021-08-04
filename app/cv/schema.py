import graphene
import graphql_jwt
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

User1 = get_user_model()


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class User(DjangoObjectType):
    class Meta:
        model = User1


class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return User1.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)



import graphene
import graphql_jwt
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

CustomUser = get_user_model()


class User(DjangoObjectType):
    class Meta:
        model = CustomUser


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class Query(graphene.ObjectType):
    no_query = graphene.Field(graphene.String)

    def resolve_no_query(self, info):
        return 'Non query'


schema = graphene.Schema(query=Query, mutation=Mutation)



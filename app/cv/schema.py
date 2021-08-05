import graphene
import graphql_jwt
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

CustomUser = get_user_model()


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class User(DjangoObjectType):
    class Meta:
        model = CustomUser


class Query(graphene.ObjectType):
    users = graphene.List(User)
    whoami = graphene.Field(User)

    @login_required
    def resolve_users(self, info):
        return CustomUser.objects.all()

    # @login_required
    def resolve_whoami(self, info):
        return CustomUser.objects.all()[0]


schema = graphene.Schema(query=Query, mutation=Mutation)



import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import User as UserModel, Post as PostModel
from app import db


class UserType(SQLAlchemyObjectType):
    class Meta:
        model = UserModel

class PostType(SQLAlchemyObjectType):
    class Meta:
        model = PostModel

class AddNewUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(root, info, username, email, password):
        new_user = UserModel(username=username, email=email, password=password)
        return AddNewUser(user=new_user)


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    posts = graphene.List(PostType)
    user = graphene.Field(UserType, user_id=graphene.ID(required=True))
    search_users = graphene.List(UserType, username=graphene.String(), email=graphene.String())

    def resolve_users(root, info):
        query = db.select(UserModel)
        return db.session.scalars(query)

    def resolve_posts(root, info):
        query = db.select(PostModel)
        return db.session.scalars(query)

    def resolve_user(root, info, user_id):
        user = db.session.get(UserModel, user_id)
        return user

    def resolve_search_users(root, info, username=None, email=None):
        query = db.select(UserModel)
        if username:
            query = query.where(UserModel.username.ilike(f"%{username}%"))
        if email:
            query = query.where(UserModel.email.ilike(f"%{email}%"))
        return db.session.scalars(query)


class Mutation(graphene.ObjectType):
    add_new_user = AddNewUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

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

class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    posts = graphene.List(PostType)

    def resolve_users(root, info):
        query = db.select(UserModel)
        return db.session.scalars(query)

    def resolve_posts(root, info):
        query = db.select(PostModel)
        return db.session.scalars(query)


schema = graphene.Schema(query=Query)

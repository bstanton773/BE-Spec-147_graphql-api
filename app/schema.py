import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import User as UserModel
from app import db


class UserType(SQLAlchemyObjectType):
    class Meta:
        model = UserModel



class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(root, info):
        query = db.select(UserModel)
        return db.session.scalars(query)


schema = graphene.Schema(query=Query)

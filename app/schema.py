import graphene


class Query(graphene.ObjectType):
    test = graphene.String()
    name = graphene.String()

    def resolve_test(root, info):
        return 'This is a test string, how are you today!'

    def resolve_name(root, info):
        return 'Brian'


schema = graphene.Schema(query=Query)

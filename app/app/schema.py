import graphene
import si_stock.schema
import user.schema
import assistencia_tecnica.schema
import sondagemIS.schema
import graphql_jwt


class Query(si_stock.schema.Query, user.schema.Query, assistencia_tecnica.schema.Query, sondagemIS.schema.Query, graphene.ObjectType):
    pass

class Mutation(si_stock.schema.Mutation, user.schema.Mutation, assistencia_tecnica.schema.Mutation, sondagemIS.schema.Mutation, graphene.ObjectType):
    # token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # verify_token = graphql_jwt.Verify.Field()
    # refresh_token = graphql_jwt.Refresh.Field()
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

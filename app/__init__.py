from ariadne import ObjectType, SubscriptionType, make_executable_schema
from graphql.type import GraphQLResolveInfo
from typing import Any, AsyncGenerator
from ariadne import gql
from ariadne.asgi import GraphQL

query_typedef = gql("""
    type Query {
        ping: String!
    }
""")

subscription_typedef = gql("""
    type Subscription {
        counter: Int!
    }
""")

query = ObjectType('Query')

@query.field('ping')
def resolve_ping(_, info, creator=None):
    return 'pong'

subscription = SubscriptionType()

@subscription.source('counter')
async def counter_generator(obj: Any, info: GraphQLResolveInfo) -> AsyncGenerator[int, None]:
    for i in range(5):
        await asyncio.sleep(1)
        yield i

@subscription.field('counter')
def counter_resolver(count: int, info: GraphQLResolveInfo) -> int:
    return count + 1

type_defs = [query_typedef, subscription_typedef]
resolvers = [query, subscription]

schema = make_executable_schema(type_defs, resolvers)
app = GraphQL(schema, debug=True)

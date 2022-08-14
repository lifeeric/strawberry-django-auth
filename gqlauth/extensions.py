from inspect import isawaitable

from graphql import GraphQLResolveInfo
from strawberry.utils.await_maybe import AwaitableOrValue
from strawberry_django_jwt.exceptions import JSONWebTokenError
from strawberry_django_jwt.middleware import (
    AsyncJSONWebTokenMiddleware,
    JSONWebTokenMiddleware,
)

__all__ = ["GqlAuthJSONWebTokenMiddleware", "AsyncJSONWebTokenMiddleware"]


class GqlAuthJSONWebTokenMiddleware(JSONWebTokenMiddleware):
    """
    see  https://github.com/KundaPanda/strawberry-django-jwt/issues/348

    Main advantage is to let the mutation handle the
    unauthenticated error. Instead of an actual error,
    we can return e.g. success=False errors=Unauthenticated
    """

    def resolve(self, _next, root, info: GraphQLResolveInfo, *args, **kwargs):
        try:
            res = super().resolve(_next, root, info, *args, **kwargs)
            return res
        except JSONWebTokenError:
            return _next(root, info, **kwargs)


class GqlAuthAsyncJSONWebTokenMiddleware(AsyncJSONWebTokenMiddleware):
    def on_request_start(self) -> AwaitableOrValue[None]:
        print(2)

    async def resolve(self, _next, root, info: GraphQLResolveInfo, *args, **kwargs):
        try:
            return await super().resolve(_next, root, info, *args, **kwargs)
        except JSONWebTokenError:
            result = _next(root, info, **kwargs)
            if isawaitable(result):
                return await result
            return result

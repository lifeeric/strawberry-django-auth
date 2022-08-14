"""
This would be to test that users can implement authentications on
Their own resolvers.
"""
from typing import Union

import strawberry
from strawberry.tools import merge_types
from strawberry.types import Info


@strawberry.type
class Apple:
    @strawberry.field
    def color(self, info: Info) -> Union[str | int]:
        return "green"


ExternalQueries = merge_types("ExternalQueries", (Apple,))

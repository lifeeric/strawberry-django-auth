from strawberry.types import Info

from tests.testCases import TestBase


class TestExternalUsages(TestBase):
    @classmethod
    def test_login_required_injects_info(cls, db_verified_user_status):
        cls.make_request(
            query="""

            """
        )
        res = ...
        assert isinstance(res, Info)

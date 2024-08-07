# coding: utf-8

"""
    Morph API

    REST API of the multi-node/multi-drive Morph object storage.

    The version of the OpenAPI document: v0.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.user_change_storage_quota_request import UserChangeStorageQuotaRequest

class TestUserChangeStorageQuotaRequest(unittest.TestCase):
    """UserChangeStorageQuotaRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserChangeStorageQuotaRequest:
        """Test UserChangeStorageQuotaRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserChangeStorageQuotaRequest`
        """
        model = UserChangeStorageQuotaRequest()
        if include_optional:
            return UserChangeStorageQuotaRequest(
                size = 56
            )
        else:
            return UserChangeStorageQuotaRequest(
                size = 56,
        )
        """

    def testUserChangeStorageQuotaRequest(self):
        """Test UserChangeStorageQuotaRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

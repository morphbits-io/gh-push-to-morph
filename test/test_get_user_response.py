# coding: utf-8

"""
    Morph API

    REST API of the multi-node/multi-drive Morph object storage.

    The version of the OpenAPI document: v0.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.get_user_response import GetUserResponse

class TestGetUserResponse(unittest.TestCase):
    """GetUserResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUserResponse:
        """Test GetUserResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUserResponse`
        """
        model = GetUserResponse()
        if include_optional:
            return GetUserResponse(
                key = ''
            )
        else:
            return GetUserResponse(
                key = '',
        )
        """

    def testGetUserResponse(self):
        """Test GetUserResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
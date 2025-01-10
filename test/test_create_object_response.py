# coding: utf-8

"""
    Morph API

    REST API of the multi-node/multi-drive Morph object storage.

    The version of the OpenAPI document: v0.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_object_response import CreateObjectResponse

class TestCreateObjectResponse(unittest.TestCase):
    """CreateObjectResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateObjectResponse:
        """Test CreateObjectResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateObjectResponse`
        """
        model = CreateObjectResponse()
        if include_optional:
            return CreateObjectResponse(
                oid = '2z2ipYCDc5uWfNQTXeuYzv2pAGrLASKkRFXkUpzMsEJu'
            )
        else:
            return CreateObjectResponse(
                oid = '2z2ipYCDc5uWfNQTXeuYzv2pAGrLASKkRFXkUpzMsEJu',
        )
        """

    def testCreateObjectResponse(self):
        """Test CreateObjectResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

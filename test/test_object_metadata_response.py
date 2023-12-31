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

from openapi_client.models.object_metadata_response import ObjectMetadataResponse

class TestObjectMetadataResponse(unittest.TestCase):
    """ObjectMetadataResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObjectMetadataResponse:
        """Test ObjectMetadataResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObjectMetadataResponse`
        """
        model = ObjectMetadataResponse()
        if include_optional:
            return ObjectMetadataResponse(
                creation_date = '2022-11-21T07:12:42.686806470Z',
                size = 0,
                file_name = 'space.png',
                content_type = 'application/octet-stream'
            )
        else:
            return ObjectMetadataResponse(
                creation_date = '2022-11-21T07:12:42.686806470Z',
                size = 0,
                file_name = 'space.png',
                content_type = 'application/octet-stream',
        )
        """

    def testObjectMetadataResponse(self):
        """Test ObjectMetadataResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

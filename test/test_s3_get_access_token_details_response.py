# coding: utf-8

"""
    Morph API

    REST API of the multi-node/multi-drive Morph object storage.

    The version of the OpenAPI document: v0.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.s3_get_access_token_details_response import S3GetAccessTokenDetailsResponse

class TestS3GetAccessTokenDetailsResponse(unittest.TestCase):
    """S3GetAccessTokenDetailsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> S3GetAccessTokenDetailsResponse:
        """Test S3GetAccessTokenDetailsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `S3GetAccessTokenDetailsResponse`
        """
        model = S3GetAccessTokenDetailsResponse()
        if include_optional:
            return S3GetAccessTokenDetailsResponse(
                token = openapi_client.models.s3_detailed_token_info.S3DetailedTokenInfo(
                    create_bucket = True, 
                    delete_bucket = True, 
                    set_bucket_eacl = True, 
                    read_content = True, 
                    read_headers = True, 
                    create = True, 
                    delete = True, 
                    expires_at = '2022-11-21T07:12:42.686806470Z', 
                    created_at = '2022-11-21T07:12:42.686806470Z', 
                    name = '', 
                    container_name = '', )
            )
        else:
            return S3GetAccessTokenDetailsResponse(
                token = openapi_client.models.s3_detailed_token_info.S3DetailedTokenInfo(
                    create_bucket = True, 
                    delete_bucket = True, 
                    set_bucket_eacl = True, 
                    read_content = True, 
                    read_headers = True, 
                    create = True, 
                    delete = True, 
                    expires_at = '2022-11-21T07:12:42.686806470Z', 
                    created_at = '2022-11-21T07:12:42.686806470Z', 
                    name = '', 
                    container_name = '', ),
        )
        """

    def testS3GetAccessTokenDetailsResponse(self):
        """Test S3GetAccessTokenDetailsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

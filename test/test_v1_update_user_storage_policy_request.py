# coding: utf-8

"""
    Morph API

    REST API of the multi-node/multi-drive Morph object storage.

    The version of the OpenAPI document: v0.15.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.v1_update_user_storage_policy_request import V1UpdateUserStoragePolicyRequest

class TestV1UpdateUserStoragePolicyRequest(unittest.TestCase):
    """V1UpdateUserStoragePolicyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1UpdateUserStoragePolicyRequest:
        """Test V1UpdateUserStoragePolicyRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1UpdateUserStoragePolicyRequest`
        """
        model = V1UpdateUserStoragePolicyRequest()
        if include_optional:
            return V1UpdateUserStoragePolicyRequest(
                policy = openapi_client.models.storage_policy.StoragePolicy(
                    replicas = [
                        openapi_client.models.replica.Replica(
                            count = 56, 
                            selector = '', )
                        ], 
                    placement_factor = 56, 
                    selectors = [
                        openapi_client.models.selector.Selector(
                            name = '', 
                            count = 56, 
                            attribute = '', 
                            filter = '', 
                            clause = [
                                'SAME'
                                ], )
                        ], 
                    filters = [
                        openapi_client.models.placement_filter.PlacementFilter(
                            name = '', 
                            key = '', 
                            op = [
                                'EQ'
                                ], 
                            value = '', 
                            filters = [
                                openapi_client.models.placement_filter.PlacementFilter(
                                    name = '', 
                                    key = '', 
                                    op = [
                                        'EQ'
                                        ], 
                                    value = '', 
                                    filters = [
                                        
                                        ], )
                                ], )
                        ], )
            )
        else:
            return V1UpdateUserStoragePolicyRequest(
                policy = openapi_client.models.storage_policy.StoragePolicy(
                    replicas = [
                        openapi_client.models.replica.Replica(
                            count = 56, 
                            selector = '', )
                        ], 
                    placement_factor = 56, 
                    selectors = [
                        openapi_client.models.selector.Selector(
                            name = '', 
                            count = 56, 
                            attribute = '', 
                            filter = '', 
                            clause = [
                                'SAME'
                                ], )
                        ], 
                    filters = [
                        openapi_client.models.placement_filter.PlacementFilter(
                            name = '', 
                            key = '', 
                            op = [
                                'EQ'
                                ], 
                            value = '', 
                            filters = [
                                openapi_client.models.placement_filter.PlacementFilter(
                                    name = '', 
                                    key = '', 
                                    op = [
                                        'EQ'
                                        ], 
                                    value = '', 
                                    filters = [
                                        
                                        ], )
                                ], )
                        ], ),
        )
        """

    def testV1UpdateUserStoragePolicyRequest(self):
        """Test V1UpdateUserStoragePolicyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

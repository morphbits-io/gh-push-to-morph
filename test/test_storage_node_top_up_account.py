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

from openapi_client.models.storage_node_top_up_account import StorageNodeTopUpAccount

class TestStorageNodeTopUpAccount(unittest.TestCase):
    """StorageNodeTopUpAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StorageNodeTopUpAccount:
        """Test StorageNodeTopUpAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StorageNodeTopUpAccount`
        """
        model = StorageNodeTopUpAccount()
        if include_optional:
            return StorageNodeTopUpAccount(
                address = 'Nhfg3TbpwogLvDGVvAvqyThbsHgoSUKwtn'
            )
        else:
            return StorageNodeTopUpAccount(
                address = 'Nhfg3TbpwogLvDGVvAvqyThbsHgoSUKwtn',
        )
        """

    def testStorageNodeTopUpAccount(self):
        """Test StorageNodeTopUpAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

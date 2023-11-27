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

from openapi_client.models.record_target import RecordTarget

class TestRecordTarget(unittest.TestCase):
    """RecordTarget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecordTarget:
        """Test RecordTarget
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecordTarget`
        """
        model = RecordTarget()
        if include_optional:
            return RecordTarget(
                role = [
                    'USER'
                    ],
                keys = [
                    ''
                    ]
            )
        else:
            return RecordTarget(
                role = [
                    'USER'
                    ],
                keys = [
                    ''
                    ],
        )
        """

    def testRecordTarget(self):
        """Test RecordTarget"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
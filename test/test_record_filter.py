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

from openapi_client.models.record_filter import RecordFilter

class TestRecordFilter(unittest.TestCase):
    """RecordFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecordFilter:
        """Test RecordFilter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecordFilter`
        """
        model = RecordFilter()
        if include_optional:
            return RecordFilter(
                header_type = [
                    'REQUEST'
                    ],
                match_type = [
                    'STRING_EQUAL'
                    ],
                key = '',
                value = ''
            )
        else:
            return RecordFilter(
                header_type = [
                    'REQUEST'
                    ],
                match_type = [
                    'STRING_EQUAL'
                    ],
                key = '',
                value = '',
        )
        """

    def testRecordFilter(self):
        """Test RecordFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

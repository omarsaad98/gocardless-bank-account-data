# coding: utf-8

"""
    GoCardless Bank Account Data API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0 (v2)
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gocardless_bankaccountdata
from gocardless_bankaccountdata.api.requisitions_api import RequisitionsApi  # noqa: E501
from gocardless_bankaccountdata.rest import ApiException


class TestRequisitionsApi(unittest.TestCase):
    """RequisitionsApi unit test stubs"""

    def setUp(self):
        self.api = RequisitionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_requisition(self):
        """Test case for create_requisition

        """
        pass

    def test_delete_requisition_by_id(self):
        """Test case for delete_requisition_by_id

        """
        pass

    def test_requisition_by_id(self):
        """Test case for requisition_by_id

        """
        pass

    def test_retrieve_all_requisitions(self):
        """Test case for retrieve_all_requisitions

        """
        pass


if __name__ == '__main__':
    unittest.main()

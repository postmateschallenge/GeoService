# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAddressController(BaseTestCase):
    """AddressController integration test stubs"""

    def test_get_lat_lng_with_addr(self):
        """Test case for get_lat_lng_with_addr

        get latitude and longitude of an address
        """
        query_string = [('addr', 'addr_example')]
        response = self.client.open(
            '/PostmatesGeoServices/PostmatesGeoServices/1.0.0/Address',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

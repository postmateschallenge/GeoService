import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server import util


def get_lat_lng_with_addr(addr=None):  # noqa: E501
    """get latitude and longitude of an address

    By passing in the address, you can get latitude and longitude of an it  # noqa: E501

    :param addr: pass an address
    :type addr: str

    :rtype: ApiResponse
    """
    return 'do some magic!'

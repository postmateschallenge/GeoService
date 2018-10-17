import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server import util

import urllib
import json
import re

SERVICE_PROVIDERS = ['here', 'google']
PRIMARY_SERVICE = SERVICE_PROVIDERS[0]
SECONDARY_SERVICE = SERVICE_PROVIDERS[1]

def url2Request(service=PRIMARY_SERVICE, addr=""):
    if service == PRIMARY_SERVICE:
        urlBase = 'https://geocoder.api.here.com/6.2/geocode.json'
        query = {}
        query['app_id'] = 'ontaBB1aZtjPd7dgm8E1'
        query['app_code'] = 'iMhp5B38Yq23C1eYVUm5og'
        query['locationattributes'] = 'none'
        query['searchtext'] = addr
        print((key + '=' + query.get(key) for key in query))
        queryStr = '&'.join((key + '=' + query.get(key) for key in query))
        return '{0}?{1}'.format(urlBase, queryStr)
        
def get_lat_lng_with_addr(addr=None):  # noqa: E501
    """get latitude and longitude of an address

    By passing in the address, you can get latitude and longitude of an it  # noqa: E501

    :param addr: pass an address
    :type addr: str

    :rtype: ApiResponse
    """
    addr = '+'.join(re.findall(r"[\w',]+", addr))
    _url2Request = url2Request(PRIMARY_SERVICE, addr)
    print(_url2Request)
    primaryServiceUnavaliable = False
    returnJson = {}
    try:
        with urllib.request.urlopen(_url2Request) as r:
            result = json.load(r)
            if not result or not result.get('Response'):
                primaryServiceUnavaliable = True
            else:
                if (len(result.get('Response').get('View')) > 0 and 
                len(result.get('Response').get('View')[0].get('Result')) > 0):
                    coordinates = [p.get('Location').get('NavigationPosition')[0] for p in result.get('Response').get('View')[0].get('Result')]
                    returnJson = {'PossibleLocations': coordinates}
    except:
        primaryServiceUnavaliable = True
    if primaryServiceUnavaliable:
        pass        
    return returnJson


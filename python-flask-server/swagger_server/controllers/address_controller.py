import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server import util

import urllib
import json
import re

SERVICE_PROVIDERS = ['google', 'here']
GOOGLE_SERVICE = 'google'
HERE_SERVICE= 'here'
PRIMARY_SERVICE = SERVICE_PROVIDERS[0]
SECONDARY_SERVICE = SERVICE_PROVIDERS[1]
FAILED_RESPONSE = {'Failed': []}

def url2Request(service=PRIMARY_SERVICE, addr=""):
    urlBase = 'localhost'
    queryStr = ''
    if service == HERE_SERVICE:
        urlBase = 'https://geocoder.api.here.com/6.2/geocode.json'
        query = {}
        query['app_id'] = 'ontaBB1aZtjPd7dgm8E1'
        query['app_code'] = 'iMhp5B38Yq23C1eYVUm5og'
        query['locationattributes'] = 'none'
        query['searchtext'] = addr
        queryStr = '&'.join((key + '=' + query.get(key) for key in query))
    elif service == GOOGLE_SERVICE:
        query = {}
        urlBase = 'https://maps.googleapis.com/maps/api/geocode/json'
        query['key'] = 'AIzaSyDKw7bn1fQUoqqAaBF6teXScWPxl8ByIkk'
        query['address'] = addr
        queryStr = '&'.join((key + '=' + query.get(key) for key in query))
    return '{0}?{1}'.format(urlBase, queryStr)


def serviceResultTranslate(service, result):
    returnJson = {}
    selectedServiceUnavaliable = False
    print(result)
    if service == GOOGLE_SERVICE:
        """
        Google service only returns one most possible location
        """
        if not result or not result.get('results'):
            selectedServiceUnavaliable = True
            returnJson = FAILED_RESPONSE
        else:
            coordinate = result.get('results')[0].get('geometry').get('location')
            returnJson = {'Success': {'PossibleLocations': [{'lat': coordinate.get('lat'), 'lng': coordinate.get('lng')}]}}
    elif service == HERE_SERVICE:
        """
        Here service does the fuzzy search with address, we can get multiple possible locations
        """
        if not result or not result.get('Response'):
            selectedServiceUnavaliable = True
            returnJson = FAILED_RESPONSE
        else:
            if (len(result.get('Response').get('View')) > 0 and 
            len(result.get('Response').get('View')[0].get('Result')) > 0):
                coordinates = [p.get('Location').get('NavigationPosition')[0] for p in result.get('Response').get('View')[0].get('Result')]
                coordinates = [{'lat': c.get('Latitude'), 'lng': c.get('Longitude')} for c in coordinates]
                returnJson = {'Success': {'PossibleLocations': coordinates}}
            else:
                returnJson = {'Success': {'PossibleLocations': []}}
    return selectedServiceUnavaliable, returnJson

def get_lat_lng_with_addr(addr=None):  # noqa: E501
    """get latitude and longitude of an address

    By passing in the address, you can get latitude and longitude of an it  # noqa: E501

    :param addr: pass an address
    :type addr: str

    :rtype: ApiResponse
    """
    addr = '+'.join(re.findall(r"[\w',]+", addr))
    primaryServiceUnavaliable = False
    returnJson = {}
    try:
        _url2Request = url2Request(PRIMARY_SERVICE, addr)
        with urllib.request.urlopen(_url2Request) as r:
            result = json.load(r)
            primaryServiceUnavaliable, returnJson = serviceResultTranslate(PRIMARY_SERVICE, result)
    except:
        primaryServiceUnavaliable = True
    if primaryServiceUnavaliable:
        _url2Request = url2Request(SECONDARY_SERVICE, addr)
        try:
            with urllib.request.urlopen(_url2Request) as r:
                result = json.load(r)
                primaryServiceUnavaliable, returnJson = serviceResultTranslate(SECONDARY_SERVICE, result)
        except:
            returnJson = FAILED_RESPONSE
    return returnJson
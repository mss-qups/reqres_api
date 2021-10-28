
from test_data.api_enpoints import resources, single_resource, single_resource_not_found
from test_data.common_data import data_from_server


def response_resources_get():
    """returns response as json and status"""
    res = data_from_server("GET", resources)
    return res.json(), res.status_code


def response_single_resource_get():
    """returns response as json and status code"""
    res = data_from_server("GET", single_resource)
    return res.json(), res.status_code


def response_single_resource_not_found():
    """returns single user not found as json and status code"""
    res = data_from_server("GET", single_resource_not_found)
    return res.json(), res.status_code

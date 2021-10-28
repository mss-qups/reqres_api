from test_data.api_enpoints import users_endpoint, single_user, single_user_not_found
from test_data.common_data import data_from_server
from test_data.payloads import user


def response_users():
    """returns response in json and status for users get"""
    res = data_from_server("GET", users_endpoint)
    return res.json(), res.status_code
print(response_users())

def response_single_user():
    """returns response in json and status for user get"""
    res = data_from_server("GET", single_user)
    return res.json(), res.status_code


def response_single_user_not_found():
    """returns response in json and status for user not found get"""
    res = data_from_server("GET", single_user_not_found)
    return res.json(), res.status_code


def response_create_user():
    """returns response for post user and status code"""
    res = data_from_server("POST", endpoint=users_endpoint, params=user)
    return res.json(), res.status_code


def response_update_user():
    """returns response for updating user and status code"""
    res = data_from_server("PUT", endpoint=users_endpoint, params=user)
    return res.json(), res.status_code


def response_update_user_patch():
    """returns response for updating user and status code - patch"""
    res = data_from_server("PATCH", endpoint=users_endpoint, params=user)
    return res.json(), res.status_code


def response_delete_user():
    """returns response for deleting user and status code - DELETE"""
    res = data_from_server("DELETE", endpoint=users_endpoint, params=single_user)
    return res.status_code

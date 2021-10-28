from test_data.api_enpoints import register_endpoint
from test_data.payloads import user_to_register, only_email, only_password
from test_data.common_data import data_from_server
from test_data.headers import headers_post


def response_signup_valid():
    """returns response and status for signup with only email"""
    res = data_from_server("POST", register_endpoint, headers=headers_post, params=user_to_register)
    return res.json(), res.status_code


def response_signup_email():
    """returns response and status for signup with only email"""
    res = data_from_server("POST", register_endpoint, headers=headers_post, params=only_email)
    return res.json(), res.status_code


def response_signup_password():
    """returns response and status for signup with only email"""
    res = data_from_server("POST", register_endpoint, headers=headers_post, params=only_password)
    return res.json(), res.status_code
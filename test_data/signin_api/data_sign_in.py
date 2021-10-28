from test_data.api_enpoints import login_endpoint
from test_data.payloads import only_email, only_password, user_to_login, invalid_login_detail
from test_data.common_data import data_from_server
from test_data.headers import headers_post


def response_sign_in_valid():
    """returns response and status for login with only email password"""
    res = data_from_server("POST", login_endpoint, headers_post, params=user_to_login)
    return res.json(), res.status_code


def response_sign_in_invalid_email():
    """returns response for invalid email sign in"""
    res = data_from_server("POST", login_endpoint, headers=headers_post, params=invalid_login_detail)
    return res.json(), res.status_code


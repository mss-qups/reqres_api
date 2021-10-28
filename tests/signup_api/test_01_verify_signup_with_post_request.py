import allure
from test_data.signup_api.data_sign_up import signup_response
from test_data.payloads import new_user


@allure.step('Signup api, status code validation')
def test_c115_01_status_code_is_201():
    _, status_code = signup_response
    assert status_code == 201


@allure.step("Signup api, body not none validation")
def test_c115_02_response_body_not_none():
    response_body, _ = signup_response
    assert response_body is not None


@allure.step("Signup api, body field email validation")
def test_c115_03_body_field_email():
    response_body, _ = signup_response
    assert response_body['email'] == new_user
    assert 'email' in response_body


@allure.step("Signup api, body field token validation")
def test_c115_04_body_field_token():
    response_body, _ = signup_response
    assert 'token' in response_body

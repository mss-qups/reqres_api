import allure
from test_data.signin_api.data_sign_in import valid_sign_in_response


@allure.step('Signin api, status code validation')
def test_c115_01_status_code_is_200():
    _, status_code = valid_sign_in_response()
    assert status_code == 200


@allure.step("Signin api, body not none validation")
def test_c115_02_response_body_not_none():
    response_body, _ = valid_sign_in_response()
    assert response_body is not None


@allure.step("Signin api, body field email  validation")
def test_c115_03_body_field_email():
    response_body, _ = valid_sign_in_response()
    assert response_body['email'] == "sompod123@gmail.com"


@allure.step("Signin api, body field token validation")
def test_c115_04_body_field_token():
    response_body, _ = valid_sign_in_response()
    assert 'token' in response_body

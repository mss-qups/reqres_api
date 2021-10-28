import allure
from test_data.signin_api.data_sign_in import assert_response_status, assert_response_body_none, assert_error_message_only_email


@allure.step('Signin api, status code validation')
def test_c112_01_status_code_is_400():
    assert_response_status(400)


@allure.step("Signin api, response body not none validation")
def test_c112_02_response_body_not_none():
    assert_response_body_none(email=True)


@allure.step("Signin api, error message validation")
def test_c112_03_error_message():
    assert_error_message_only_email("You must supply a password")

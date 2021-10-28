import allure
from test_data.signin_api.data_sign_in import assert_response_status, assert_response_body_none, response_for_only_password


@allure.step('Signin api, status code validation')
def test_c113_01_status_code_is_400(password=True):
    assert_response_status(400)


@allure.step("Signin api, response body not none validation")
def test_c113_02_response_body_not_none():
    assert_response_body_none(password=True)


@allure.step("Signin api, error message validation")
def test_c113_03_error_message():
    assert response_for_only_password()['errors'][0]["message"] == "Email must be valid"


@allure.step("Signin api, required field email validation")
def test_c113_04_required_field_email():
    assert response_for_only_password()['errors'][0]["field"] == "email"

import allure
from test_data.signup_api.data_sign_up import response_signup_password


@allure.step('Signin api, status code validation')
def test_c113_01_status_code_is_400():
    _, status = response_signup_password()
    assert status == 400


@allure.step("Signup api, response body not none validation")
def test_c113_02_response_body_not_none():
    body, _ = response_signup_password()
    assert body is not None


@allure.step("Signup api, error message validation")
def test_c113_03_error_message():
    body, _ = response_signup_password()
    assert body['errors'][0]["message"] == "Email must be valid"


@allure.step("Signup api, required field email validation")
def test_c113_04_required_field_email():
    body, _ = response_signup_password()
    assert body['errors'][0]["field"] == "email"

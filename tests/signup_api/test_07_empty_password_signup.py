import allure
from test_data.signup_api.data_sign_up import response_signup_valid


@allure.step('Signup api, status code validation')
def test_c112_01_status_code_is_400():
    assert response_signup_valid()[1] == 400


@allure.step("Signup api, response body not none validation")
def test_c112_02_response_body_not_none():
    assert response_signup_valid()[0] is not None


@allure.step("Signup api, error message validation")
def test_c112_03_error_message():
    assert response_signup_valid()[0]['errors'][0]["message"] == "Password must be 8 character long"


@allure.step("Signup api, required field password validation")
def test_c112_04_required_field_password():
    assert response_signup_valid()[0]['errors'][0]["field"] == "password"

import allure

from test_data.signup_api.data_sign_up import response_signup_email


@allure.step("signup user only email")
def test_01_user_register_only_email():
    _, status_code = response_signup_email()
    assert status_code == 400


@allure.step("signup user response body verification only email")
def test_02_user_register_response_body_email():
    response_body, _ = response_signup_email()
    assert "error" in response_body
    assert response_body['error'] == "Missing password"

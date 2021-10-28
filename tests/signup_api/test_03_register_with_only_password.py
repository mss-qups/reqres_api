import allure

from test_data.signup_api.data_sign_up import response_signup_password


@allure.step("signup user only password")
def test_01_user_register_only_password():
    _, status_code = response_signup_password()
    assert status_code == 400


@allure.step("signup user response body verification only password")
def test_02_user_register_response_body_password():
    response_body, _ = response_signup_password()
    assert "error" in response_body
    assert response_body['error'] == "Missing email or username"

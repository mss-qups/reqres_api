import allure
from test_data.signup_api.data_sign_up import response_signup_valid


@allure.step("signup user")
def test_01_user_register_valid():
    _, status_code = response_signup_valid()
    assert status_code == 200


@allure.step("signup user response body verification")
def test_02_user_register_response_body():
    response_body, _ = response_signup_valid()
    assert "id" in response_body
    assert "token" in response_body

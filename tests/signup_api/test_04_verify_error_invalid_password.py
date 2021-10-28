import allure
from test_data.signup_api.data_sign_up import response_signup_invalid_password


@allure.step('Signup api, status code validation')
def test_01_invalid_email_signup():
    _, status_code = response_signup_invalid_password()
    assert status_code == 400


@allure.step("Signup api, invalid password")
def test_02_invalid_email_signup():
    response_body, _ = response_signup_invalid_password()
    assert response_body['errors'][3]['message'] == 'Password must contain a special character [!@#$%^&*]'

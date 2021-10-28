import allure
from test_data.signup_api.data_sign_up import response_signup_existing_request


@allure.step('Signup api, existing user')
def test_01_existing_email_signup():
    _, status_code = response_signup_existing_request()
    assert status_code == 400


@allure.step("Signup api, existing user")
def test_02_existing_email_signup():
    response_body, _ = response_signup_existing_request()
    assert response_body['errors'][0]['message'] == 'Email in use'

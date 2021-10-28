import allure
from test_data.signup_api.data_sign_up import response_signup_get_request


@allure.step('Signup api, status code validation')
def test_c116_01_status_code_is_404():
    _, status_code = response_signup_get_request()
    assert status_code == 404


@allure.step("Signup api, body not none validation")
def test_c116_02_response_body_not_none():
    response_body, _ = response_signup_get_request()
    assert response_body is not None


@allure.step("Signup api, error message validation")
def test_c116_03_error_message():
    response_body, _ = response_signup_get_request()
    assert response_body['errors'][0]["message"] == "Not found"

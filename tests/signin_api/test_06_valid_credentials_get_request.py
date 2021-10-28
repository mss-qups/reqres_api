import allure
from test_data.signin_api.data_sign_in import response_sign_in_get_request


@allure.step('Signin api, status code validation')
def test_c116_01_status_code_is_404():
    assert response_sign_in_get_request()[1] == 404


@allure.step("Signin api, body not none validation")
def test_c116_02_response_body_not_none():
    assert response_sign_in_get_request()[0] is not None


@allure.step("Signin api, error message validation")
def test_c116_03_error_message():
    assert response_sign_in_get_request()[0]['errors'][0]["message"] == "Not found"

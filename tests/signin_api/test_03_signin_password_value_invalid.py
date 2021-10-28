import allure
from test_data.signin_api.data_sign_in import response_sign_in_invalid_password


@allure.step('Signin api, status code invalid data')
def test_c114_01_status_code_is_400():
    response_body, status_code = response_sign_in_invalid_password()
    assert status_code == 400


@allure.step("Signin api, invalid email")
def test_c114_02_error_msg():
    response_body, status_code = response_sign_in_invalid_password()
    assert response_body['errors'][0]['message'] == 'Email must be valid'
    assert response_body['errors'][1]['message'] == 'You must supply a password'




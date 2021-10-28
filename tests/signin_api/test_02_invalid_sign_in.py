import allure

from test_data.signin_api.data_sign_in import response_sign_in_invalid_email


@allure.step("signing with invalid details")
def test_01_user_sign_in_valid_credentials():
    _, status_code = response_sign_in_invalid_email()
    assert status_code == 400


@allure.step("sign_in response body verification for invalid details")
def test_02_user_sign_in_details_body():
    response_body, _ = response_sign_in_invalid_email()
    assert response_body['error'] == 'Missing password'

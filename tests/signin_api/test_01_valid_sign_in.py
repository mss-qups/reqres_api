import allure

from test_data.signin_api.data_sign_in import response_sign_in_valid


@allure.step("signing with valid details")
def test_01_user_sign_in_valid_credentials():
    _, status_code = response_sign_in_valid()
    assert status_code == 200


@allure.step("sign_in response body verification")
def test_02_user_sign_in_details_body():
    response_body, _ = response_sign_in_valid()
    assert 'token' in response_body

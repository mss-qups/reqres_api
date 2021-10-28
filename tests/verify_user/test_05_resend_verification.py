import allure
from test_data.delayed_response_api.delayed_response_data import response_resend_code


@allure.step('resend code')
def test_01_resend_verification_code():
    _, status_code = response_resend_code()
    assert status_code == 200


@allure.step('Forget User Response Code')
def test_01_resend_message():
    response_body, _ = response_resend_code()
    assert 'a new Verification code sent' in response_body['message']

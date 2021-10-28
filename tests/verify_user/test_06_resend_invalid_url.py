import allure
from test_data.delayed_response_api.delayed_response_data import response_resend_code_invalid_url


@allure.step('resend invalid_url')
def test_01_resend_verifi_invalid_url():
    _, status_code = response_resend_code_invalid_url()
    assert status_code == 404
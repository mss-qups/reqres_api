import allure
from test_data.delayed_response_api.delayed_response_data import response_reset_password_get_request


@allure.step('reset password valid get')
def test_01_reset_password_valid_get():
    _, status_code = response_reset_password_get_request()
    assert status_code == 404



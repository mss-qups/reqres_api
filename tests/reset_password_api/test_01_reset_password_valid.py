import allure
from test_data.delayed_response_api.delayed_response_data import response_reset_password_valid


@allure.step('reset password valid')
def test_01_reset_password_valid():
    _, status_code = response_reset_password_valid()
    assert status_code == 200



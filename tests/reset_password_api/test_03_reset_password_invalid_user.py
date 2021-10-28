import allure
from test_data.delayed_response_api.delayed_response_data import response_reset_password_invalid_user


@allure.step('verify user invalid user')
def test_01_verify_user_invalid_user():
    _, status_code = response_reset_password_invalid_user()
    assert status_code == 404



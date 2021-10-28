import allure
from test_data.delayed_response_api.delayed_response_data import response_reset_password_new_invalid


@allure.step('Reset password, Set new password status')
def test_01_reset_set_new_password_error():
    _, status_code = response_reset_password_new_invalid()
    assert status_code == 400


@allure.step('Reset password, error message')
def test_02_reset_password_message_error_message():
    response_body, _ = response_reset_password_new_invalid()
    assert "Invalid Token" == response_body["errors"][0]["message"]

import allure
from test_data.delayed_response_api.delayed_response_data import response_reset_password_new_valid


@allure.step('Reset password, Set new password status')
def test_01_reset_set_new_():
    _, status_code = response_reset_password_new_valid()
    assert status_code == 200


@allure.step('Reset password,message')
def test_02_reset_password_message():
    response_body, _ = response_reset_password_new_valid()
    assert response_body["errors"][0]["message"]

import allure
from test_data.users_api.users_api_data import response_update_user_patch


@allure.step("update user patch")
def test_01_user_post():
    _, status_code = response_update_user_patch()
    assert status_code == 200


@allure.step("updating user with patch key verification")
def test_02_update_user_patch():
    response_body, _ = response_update_user_patch()
    assert 'updatedAt' in response_body

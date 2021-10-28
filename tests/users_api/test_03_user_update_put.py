import allure
from test_data.users_api.users_api_data import response_update_user


@allure.step("user post")
def test_01_user_post():
    _, status_code = response_update_user()
    assert status_code == 200


@allure.step("user post key verification")
def test_02_user_update():
    response_body, _ = response_update_user()
    assert 'updatedAt' in response_body

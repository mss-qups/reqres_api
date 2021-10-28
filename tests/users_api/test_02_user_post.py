import allure
from test_data.users_api.users_api_data import response_create_user


@allure.step("user post")
def test_01_user_post():
    _, status_code = response_create_user()
    assert status_code == 201


@allure.step("user post key verification")
def test_01_user_post():
    response_body, _ = response_create_user()
    assert 'id' in response_body
    assert 'createdAt' in response_body

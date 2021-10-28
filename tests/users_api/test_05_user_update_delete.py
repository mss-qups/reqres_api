import allure
from test_data.users_api.users_api_data import response_delete_user


@allure.step("delete user")
def test_01_user_delete():
    status_code = response_delete_user()
    assert status_code == 204

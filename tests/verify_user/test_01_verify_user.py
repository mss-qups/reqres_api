import allure
from test_data.resource_api.resource_data import response_verify_user


@allure.step('verify user')
def test_01_verify_user():
    _, status_code = response_verify_user()
    assert status_code == 200



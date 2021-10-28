import allure
from test_data.resource_api.resource_data import response_verify_user_invalid_url


@allure.step('verify user invalid url')
def test_01_verify_user_invalid_url():
    _, status_code = response_verify_user_invalid_url()
    assert status_code == 400



import allure
from test_data.resource_api.resource_data import response_resources_get


@allure.step('all users list')
def test_01_all_users_get_status():
    response_body, status_code = response_resources_get()
    assert status_code == 200


@allure.step('all users key verification')
def test_02_all_users_key():
    response_body, _ = response_resources_get()
    assert 'page' in response_body
    assert 'total' in response_body
    assert 'data' in response_body

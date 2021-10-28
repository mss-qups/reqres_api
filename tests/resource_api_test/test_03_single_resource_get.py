import allure
from test_data.resource_api.resource_data import response_single_resource_get


@allure.step('single resource get')
def test_01_all_users_get_status():
    response_body, status_code = response_single_resource_get()
    assert status_code == 200


@allure.step('single resource keys verification')
def test_02_all_users_key():
    response_body, _ = response_single_resource_get()
    assert 'data' in response_body
    assert response_body['data']['id'] == 2
    assert response_body['data']['name'] == 'fuchsia rose'
    assert response_body['data']['year'] == 2001


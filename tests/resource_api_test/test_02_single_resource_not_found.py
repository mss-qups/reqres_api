import allure
from test_data.resource_api.resource_data import response_single_resource_not_found


@allure.step('single resource not found')
def test_01_single_resource_not_found_status():
    response_body, status_code = response_single_resource_not_found()
    assert status_code == 404


@allure.step('single resource key verification')
def test_02_single_resource_key_verification():
    response_body, _ = response_single_resource_not_found()
    assert response_body == {}

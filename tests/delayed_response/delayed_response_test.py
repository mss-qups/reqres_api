from test_data.delayed_response_api.delayed_response_data import response_resources_get_delayed

import allure


@allure.step('Delayed response test')
def test_01_delayed_response_status():
    _, status_code, _ = response_resources_get_delayed()
    assert status_code == 200


@allure.step('Delayed response test')
def test_01_delayed_response_status():
    _, _, response_time = response_resources_get_delayed()
    assert response_time > 2.5

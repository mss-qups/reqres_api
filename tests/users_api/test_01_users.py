import allure
from test_data.users_api.users_api_data import response_users, \
    response_single_user_not_found, \
    response_single_user


@allure.step('all users list')
def test_01_all_users_get_status():
    response_body, status_code = response_users()
    assert status_code == 200


@allure.step('all users keys')
def test_02_all_users_keys():
    response_body, _ = response_users()
    assert 'page' in response_body
    assert 'per_page' in response_body
    assert 'data' in response_body
    assert 'email' in response_body[0]
    assert 'first_name' in response_body[0]
    assert 'last_name' in response_body[0]
    assert 'avatar' in response_body[0]


@allure.step("Single user get")
def test_03_single_user():
    _, status_code = response_single_user()
    assert status_code == 200


@allure.step("single user details get")
def test_c112_04_body_field_id():
    response_body, _ = response_single_user()
    assert response_body['data']['id'] == 2
    assert response_body['data']['email'] == 'janet.weaver@reqres.in'


@allure.step("single user not found")
def test__05_single_user_not_found():
    response_body, status_code = response_single_user_not_found()
    assert status_code == 404
    assert response_body == {}

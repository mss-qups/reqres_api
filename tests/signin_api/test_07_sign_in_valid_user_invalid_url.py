import allure
from test_data.signin_api.data_sign_in import valid_sign_in_invalid_url


@allure.step('Signin api, invalid url')
def test_c115_01_status_invalid_url():
    _, status_code = valid_sign_in_invalid_url()
    assert status_code == 404



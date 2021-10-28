
from test_data.api_enpoints import delayed_endpoint
from test_data.common_data import data_from_server


def response_resources_get_delayed():
    """returns response as json and status"""
    res = data_from_server("GET", delayed_endpoint)
    return res.json(), res.status_code, res.elapsed.seconds

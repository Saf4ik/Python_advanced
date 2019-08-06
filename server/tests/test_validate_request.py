from protocol import validate_request

import pytest
from datetime import datetime


@pytest.fixture
def expected_action():
    return 'test'

@pytest.fixture
def expected_data():
    return 'Some data'

@pytest.fixture
def valid_request(expected_action, expected_data):
    return {
        'action': expected_action,
        'time': datetime.now().timestamp(),
        'data': expected_data, 
    }

@pytest.fixture
def invalid_request():
    return {
        'invalid_key': 'invalid_value'
    }

def test_valid_validate_request(valid_request):
    is_valid = validate_request(valid_request)
    assert is_valid


def test_invalid_validate_request(invalid_request):
    is_valid = validate_request(invalid_request)
    assert not is_valid 
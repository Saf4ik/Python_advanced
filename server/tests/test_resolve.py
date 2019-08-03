import pytest
from actions import resolve


@pytest.fixture
def controller():
    return lambda arg: arg


@pytest.fixture
def actions(controller):
    return [
        {'action': 'Some text', 'controller': controller},
    ]


def test_resolve(actions, controller):
    resolved = resolve('Some text', actions)
    assert resolved == controller
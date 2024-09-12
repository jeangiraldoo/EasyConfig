import pytest
from config import config_manager
from app_data import easyConfig

@pytest.mark.parametrize("path, expected", [
    ("Users/Desktop", False), 
    ("C:/Users", True), 
    ("ksfakfd", False),
    ("D:", True)
])
def test_verify_path_exists(path, expected):
    assert config_manager.verify_path_exists(path) == expected

@pytest.mark.parametrize("value, expected", [
    ("minecraft->C:/Users/{easyConfig.user}/Desktop", ["minecraft", "C:/Users/{easyConfig.user}/Desktop"]),
    (" my_app ->  C:/Users/{easyConfig.user}/Documents", ["my_app", "C:/Users/{easyConfig.user}/Documents"]),
    ("single_string", ["single_string"]),
    ("   single_string_space  ", ["single_string_space"])
])
def test_get_pairs(value, expected):
    assert config_manager.get_pairs(value) == expected

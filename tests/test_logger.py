from ctypes import Structure
from src.logger_config import StructuredMessage

# Tests for StructuredMessage class

def test_outputs_structured_json():
    """ Test if the kwargs are formatted as structured json """
    message = "This is a test with kwargs"
    kwargs = {
        "key_one": "value_one",
        "key_two": "value_two"
    }
    expected_output = 'This is a test with kwargs >>> {"key_one": "value_one", "key_two": "value_two"}'
    record_to_test = StructuredMessage(message, kwargs)
    assert expected_output == str(record_to_test)

def test_outputs_message_if_no_kwargs_given():
    """ Test if message alone is outputted with no structured json """
    message = "This is a test with no kwargs"
    expected_output = "This is a test with no kwargs"
    record_to_test = StructuredMessage(message)
    assert expected_output == str(record_to_test)

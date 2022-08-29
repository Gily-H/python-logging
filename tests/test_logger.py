import logging
from src.logger_config import StructuredMessage, configure_loggers

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


# Tests for Logging Config

def test_exists_logger_regilog_with_level_debug():
    """ Test if logger named regilog exists with debug level """
    configure_loggers()
    logger = logging.getLogger("regilog")
    assert logger.isEnabledFor(10)
    assert logger.hasHandlers()

def test_exists_root_logger_with_level_warning():
    configure_loggers()
    logger = logging.getLogger("root")
    assert logger.isEnabledFor(30)
    assert logger.hasHandlers()

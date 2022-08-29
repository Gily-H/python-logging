import json
import logging
import logging.config
import logging.handlers


def configure_loggers():
    """
    Method to set the logging configuration when app starts
    """

    LOGGER_CONFIG = {
        "version": 1,
        "formatters": {
            "detailed_info": {
                "format": '%(asctime)s %(module)s:%(funcName)s:ln%(lineno)d - %(levelname)s: %(message)s'
            },
            "short_info": {
                "format": "%(asctime)s %(levelname)s: %(message)s"
            },
        },
        "handlers": {
            "rotating_file_output": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "output.log",
                "mode": "a",
                "maxBytes": 1048,
                "backupCount": 3,
                "level": "INFO",
                "formatter": "detailed_info"
            },
            "console_output": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "level": "DEBUG",
                "formatter": "detailed_info"
            }
        },
        "loggers": {
            "regilog": {
                "level": "DEBUG",
                "propagate": False,
                "handlers": ["console_output"]
            },
        },
        "root": {
            "level": "WARNING",
            "handlers": ["console_output"]
        }
    }

    logging.config.dictConfig(LOGGER_CONFIG)


class StructuredMessage:
    """ Helper class to format log messages with structured json """

    def __init__(self, message, kwargs=None):
        """
        Instantiate a message with kwargs as structured json

        :param message: plain text log message
        :param kwargs: dict of kwargs to be logged as structured json
        """
        self.message = message
        self.kwargs = kwargs

    def __str__(self):
        """ The string output of an object instance of this class """
        if self.kwargs is not None:
            return '%s >>> %s' % (self.message, json.dumps(self.kwargs))
        else:
            return self.message

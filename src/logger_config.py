import json

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

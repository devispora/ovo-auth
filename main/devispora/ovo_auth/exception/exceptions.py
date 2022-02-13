from enum import Enum


class RequestException(Exception):
    def __init__(self, message, additional_message: str = None):
        self.message = message
        self.additional_message = additional_message

    def __str__(self):
        return self.message.value


class RequestExceptionMessage(str, Enum):
    CodeNoLongerValid = 'The supplied code has expired and can no longer be used'

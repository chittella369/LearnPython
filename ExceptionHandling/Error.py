# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class InputTooSmallError(Error):
    """Raised when the entered alpahbet is smaller than the actual one"""
    pass


class InputTooLargeError(Error):
    """Raised when the entered alpahbet is larger than the actual one"""
    pass
class Error(Exception):
    """Base class"""
    pass

class AdbConnectionError(Exception):
    """Raised when ADB can't connect"""
    pass

class AdbPushError(Exception):
    """Raised when a file can't be pushed"""
    pass

class AdbPullError(Exception):
    """Raised when a file can't be pulled"""
    pass

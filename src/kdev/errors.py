"""
This module contains all specialized error classes
and utilities.
"""
import errno


class KdevError(Exception):
    """
    Base error class, all specilized error classes
    should inherit from this one.
    """
    errno: int
    message: str

    def __init__(self, message: str, errno: int = 1) -> None:
        """
        Create a new KdevError object instance with a error mesgae and error number.

        The error number defaults to `1` if one is not provided.
        """
        super().__init__(message)

        self.message = message
        self.errno = errno

    def __str__(self) -> str:
        """
        Return a user friendly string representation of the error.
        """
        return self.message
    
    def __repr__(self) -> str:
        """
        Return a more detailed not no user friendly error message.
        """
        return f'[{self.errno}] {self.message}'
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, KdevError):
            raise NotImplemented

        return repr(self) == repr(other)


class NotImplementedError(KdevError):
    """
    Error to be raisen if a feature has not been implemented.
    """
    def __init__(self)  -> None:
        """
        Create a new object instance, no params are needed,
        `errno.ENOSYS` is used as error number.
        """
        super().__init__('Function or feature not implemented', errno.ENOSYS)

"""module for decorators based on decorator patterns"""

class LoginCheck:
    """
    decorator to check is session user registered/login
    """

    def __init__(self, func):
        self.function = func

    # if single function
    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)

    # if method need to use WrapperHelper to get self from method
    def __get__(self, wrapped_instance, class_owner):
        return WrapperHelper(self, wrapped_instance)


class WrapperHelper:
    """ Callable that store wrapped class instance and decorator instance """
    def __init__(self, decorator_instance, wrapped_instance):
        self.decorator_instance = decorator_instance
        self.wrapped_instance = wrapped_instance

    def __call__(self, *args, **kwargs):
        """ Call func from decorator as object method - add decorated object instance we saved """
        if not self.wrapped_instance.user.registered:
            print("user is not registered")
        return self.decorator_instance(self.wrapped_instance, *args, **kwargs)

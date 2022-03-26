"""module with controllers"""
from datetime import date


class Controllers:
    """
    add you controllers here
    """

    @staticmethod
    def secret_front(request):
        request['data'] = date.today()

    @staticmethod
    def other_front(request):
        request['key'] = 'key'

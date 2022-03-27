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
        request['topics'] = ('Topic 1', 'Topic 2', 'Topic 3', 'Topic 4', 'Topic 5')

    @staticmethod
    def style(request):
        """
        controller to provide css as a file
        :param request:
        :return:
        """
        with open('templates/main.css') as file:
            css_file = file.read()
        request['style'] = css_file

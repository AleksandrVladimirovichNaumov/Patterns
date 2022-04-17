"""module with controllers"""
from patterns.engine import Engine
from temp_storage import LANGUAGES

server = Engine()


class Controllers:
    """
    add you controllers here
    """

    @staticmethod
    def topics(request):
        """
        controller to provide list of topics
        :param request:
        :return: -
        """
        request['topics'] = [['Topic 1', False,
                              ['SubTopic 1', 'SubTopic 2', 'SubTopic 3', 'SubTopic 4', 'SubTopic 5', 'SubTopic 6',
                               'SubTopic 7', 'SubTopic 8', 'SubTopic 9', 'SubTopic 10']],
                             ['Topic 2', False,
                              ['SubTopic 1', 'SubTopic 2', 'SubTopic 3', 'SubTopic 4', 'SubTopic 5', 'SubTopic 6',
                               'SubTopic 7', 'SubTopic 8', 'SubTopic 9', 'SubTopic 10']],
                             ['Topic 3', False,
                              ['SubTopic 1', 'SubTopic 2', 'SubTopic 3', 'SubTopic 4', 'SubTopic 5', 'SubTopic 6',
                               'SubTopic 7', 'SubTopic 8', 'SubTopic 9', 'SubTopic 10']],
                             ['Topic 4', False,
                              ['SubTopic 1', 'SubTopic 2', 'SubTopic 3', 'SubTopic 4', 'SubTopic 5', 'SubTopic 6',
                               'SubTopic 7', 'SubTopic 8', 'SubTopic 9', 'SubTopic 10']],
                             ['Topic 5', False,
                              ['SubTopic 1', 'SubTopic 2', 'SubTopic 3', 'SubTopic 4', 'SubTopic 5', 'SubTopic 6',
                               'SubTopic 7', 'SubTopic 8', 'SubTopic 9', 'SubTopic 10']],
                             ['Topic 6', False,
                              ['SubTopic 1', 'SubTopic 2', 'SubTopic 3', 'SubTopic 4', 'SubTopic 5', 'SubTopic 6',
                               'SubTopic 7', 'SubTopic 8', 'SubTopic 9', 'SubTopic 10']],
                             ['Topic 7', False,
                              ['SubTopic 1', 'SubTopic 2', 'SubTopic 3', 'SubTopic 4', 'SubTopic 5', 'SubTopic 6',
                               'SubTopic 7', 'SubTopic 8', 'SubTopic 9', 'SubTopic 10']],
                             ['Topic 8', False,
                              ['SubTopic 1', 'SubTopic 2', 'SubTopic 3', 'SubTopic 4', 'SubTopic 5', 'SubTopic 6',
                               'SubTopic 7', 'SubTopic 8', 'SubTopic 9', 'SubTopic 10']],
                             ['Topic 9', False,
                              ['SubTopic 1', 'SubTopic 2', 'SubTopic 3', 'SubTopic 4', 'SubTopic 5', 'SubTopic 6',
                               'SubTopic 7', 'SubTopic 8', 'SubTopic 9', 'SubTopic 10']],
                             ['Education & sport', False,
                              ['SubTopic 1', 'SubTopic 2', 'SubTopic 3', 'SubTopic 4', 'SubTopic 5', 'SubTopic 6',
                               'SubTopic 7', 'SubTopic 8', 'SubTopic 9', 'SubTopic 10']]
                             ]

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

    @staticmethod
    def languagues(request):
        """
        controller to provide list of languagues
        :param request:
        :return:
        """
        request['languages'] = LANGUAGES

    @staticmethod
    def words(request):
        """
        controller to provide list of languagues
        :param request:
        :return:
        """
        request['words'] = [
            ['word 1', 'word 2', 'word 3', 'word 4', 'word 5', 'word 6', 'word 7', 'word 8', 'word 9', 'word 10'],
            ['word 1', 'word 2', 'word 3', 'word 4', 'word 5', 'word 6', 'word 7', 'word 8', 'word 9', 'word 10']
        ]

    @staticmethod
    def settings(request):
        """
        controller to provide dict with settings
        :param request:
        :return:
        """
        if request.get('GET_DATA'):
            if request.get('GET_DATA').get('main_language'):
                server.set_settings('main_language', int(request['GET_DATA']['main_language']))

            if request.get('GET_DATA').get('second_language'):
                server.set_settings('second_language', int(request['GET_DATA']['second_language']))

        request['settings'] = server.settings.build()

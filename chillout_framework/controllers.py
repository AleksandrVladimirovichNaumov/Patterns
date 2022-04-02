"""module with controllers"""


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
        request['topics'] = [['Topic 1', False, ['SubTopic 1', 'SubTopic 2', 'SubTopic 3', 'SubTopic 4', 'SubTopic 5', 'SubTopic 6', 'SubTopic 7', 'SubTopic 8', 'SubTopic 9', 'SubTopic 10']],
                             ['Topic 2', False, ['SubTopic 1', 'SubTopic 2', 'SubTopic 3', 'SubTopic 4', 'SubTopic 5', 'SubTopic 6', 'SubTopic 7', 'SubTopic 8', 'SubTopic 9', 'SubTopic 10']],
                             ['Topic 3', False, ['SubTopic 1', 'SubTopic 2', 'SubTopic 3', 'SubTopic 4', 'SubTopic 5', 'SubTopic 6', 'SubTopic 7', 'SubTopic 8', 'SubTopic 9', 'SubTopic 10']],
                             ['Topic 4', False, ['SubTopic 1', 'SubTopic 2', 'SubTopic 3', 'SubTopic 4', 'SubTopic 5', 'SubTopic 6', 'SubTopic 7', 'SubTopic 8', 'SubTopic 9', 'SubTopic 10']],
                             ['Topic 5', False, ['SubTopic 1', 'SubTopic 2', 'SubTopic 3', 'SubTopic 4', 'SubTopic 5', 'SubTopic 6', 'SubTopic 7', 'SubTopic 8', 'SubTopic 9', 'SubTopic 10']],
                             ['Topic 1', False,
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
        request['languages'] = ['language_1', 'language_2', 'language_3']

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
        request['topics'] = server.database.get_menu(server.get_settings()['main_language'])

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
        request['languages'] = server.get_languages()

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

    @staticmethod
    def registration(request):
        """
        controller to service user registration
        :param request:
        :return:
        """
        if request.get('POST_DATA'):
            registration_data = request.get('POST_DATA')
            try:
                #email, password, settings, topics_progress, subtopics_progress
                server.register_user(
                    server.get_usernames(),
                    registration_data['email'],
                    registration_data["password"],
                    registration_data["password_2"],
                    server.get_settings(),
                    server.get_topics_progress(),
                    server.get_subtopics_progress()

                )
            except Exception as exception:
                print(exception)

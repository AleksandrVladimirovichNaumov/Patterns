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
        request['topics'] = server.get_menu(server.get_settings()['main_language'])

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

        if request.get('GET_DATA'):
            if request.get('GET_DATA').get('topic') and request.get('GET_DATA').get('subtopic'):
                request['words'] = server.get_app_words(int(request.get('GET_DATA').get('topic')),
                                                        int(request.get('GET_DATA').get('subtopic')))
        # request['words'] = [
        #     ['word 1', 'word 2', 'word 3', 'word 4', 'word 5', 'word 6', 'word 7', 'word 8', 'word 9', 'word 10'],
        #     ['word 1', 'word 2', 'word 3', 'word 4', 'word 5', 'word 6', 'word 7', 'word 8', 'word 9', 'word 10']
        # ]

    @staticmethod
    def settings(request):
        """
        controller to provide dict with settings
        :param request:
        :return:
        """
        if request.get('GET_DATA'):
            if request.get('GET_DATA').get('main_language'):
                server.set_setting('main_language', int(request['GET_DATA']['main_language']))

            if request.get('GET_DATA').get('second_language'):
                server.set_setting('second_language', int(request['GET_DATA']['second_language']))

        request['settings'] = server.user.settings

    @staticmethod
    def registration(request):
        """
        controller to service user registration
        :param request:
        :return:
        """
        # if request.get('POST_DATA'):
        #     registration_data = request.get('POST_DATA')
        #     try:
        #         #email, password, settings, topics_progress, subtopics_progress
        #         server.register_user(
        #             registration_data['email'],
        #             registration_data["password"],
        #         )
        #     except Exception as exception:
        #         print(exception)

        if request.get('POST_DATA'):
            if request.get('POST_DATA').get('register'):
                registration_data = request.get('POST_DATA')
                server.register_user(
                    registration_data['email'],
                    registration_data["password"],
                )

    @staticmethod
    def login(request):
        """
        controller to service user registration
        :param request:
        :return:
        """
        # if request.get('POST_DATA'):
        #     registration_data = request.get('POST_DATA')
        #     try:
        #         #email, password, settings, topics_progress, subtopics_progress
        #         server.register_user(
        #             registration_data['email'],
        #             registration_data["password"],
        #         )
        #     except Exception as exception:
        #         print(exception)

        if request.get('POST_DATA'):
            if request.get('POST_DATA').get('login'):
                registration_data = request.get('POST_DATA')
                server.login(
                    registration_data['email'],
                    registration_data["password"],
                )

    @staticmethod
    def get_user_data(request):
        """
        controller to provide registration flag of user
        :param request:
        :return:
        """
        request['user'] = server.get_user_data()

    @staticmethod
    def get_topic_progress(request):
        """
        controller to provide topic progress
        :param request:
        :return:
        """
        request['topic_progress'] = server.get_json_topic_progress()

    @staticmethod
    def get_subtopic_progress(request):
        """
        controller to provide topic progress
        :param request:
        :return:
        """
        request['subtopic_progress'] = server.get_json_subtopic_progress()

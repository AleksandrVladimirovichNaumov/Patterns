"""module with user """
import hashlib
import json


class User:
    """
    proto class for session user.
    progress and settings for unregistered user is kept only in a session.
    if session  ends progress and settings of a user erases.
    if session user login/register, progress and settings updated/added to user profile
    """

    def __init__(self):
        self.username = 'NewWordsUser'
        # which languages are selected
        self.settings = {}
        self.topics = []
        self.subtopics = []
        # topics progress
        self.topics_progress = {}
        # subtopic progress
        self.subtopics_progress = {}
        # personal info
        self.email = ''
        self.password = ''
        self.registered = False

    def generate_topic_progress(self, language_qnty, topic_qnty):
        """
        generating initial list with percentage for each topic progress
        :param language_qnty:
        :param topic_qnty:
        :return:
        """
        self.topics_progress = [[[0 for i in range(topic_qnty)]
                                 for m in range(language_qnty)]
                                for n in range(language_qnty)]
        return self

    def calculate_topic_progress(self, language_qnty):
        topics_progress = [[[ int(sum(subtopic_progress)/len(subtopic_progress)) for subtopic_progress in self.subtopics_progress[m][n]]
                                 for m in range(language_qnty)]
                                for n in range(language_qnty)]
        return topics_progress

    def generate_subtopic_progress(self, language_qnty, topic_qnty, subtopic_qnty):
        """
        generating initial list with percentage for each subtopic progress
        :param language_qnty:
        :param topic_qnty:
        :param subtopic_qnty:
        :return:
        """
        self.subtopics_progress = [[[[0 for i in range(subtopic_qnty)]
                                     for n in range(topic_qnty)]
                                    for m in range(language_qnty)]
                                   for l in range(language_qnty)]
        return self

    def generate_settings(self, dict_obj):
        """
        settings stored in dict obj. method adds or replace settings
        :param dict_obj:
        :return:
        """
        self.settings |= dict_obj
        return self

    def get_main_language(self):
        return self.settings['main_language']

    def get_second_language(self):
        return self.settings['second_language']

    def data_to_register(self, email, password_1):
        """
        creating duplicate of a user with registration details
        :param settings: settings of user
        :param email: email from form
        :param password: pass from form
        :return: copy of user instance
        """
        self.email = email
        # email is a salt for password's hash
        self.password = hashlib.sha256(bytes(password_1, 'utf-8') + bytes(email, 'utf-8')).hexdigest()
        self.registered = True
        return self.username, \
               self.email, \
               self.password, \
               json.dumps(self.settings), \
               json.dumps(self.subtopics_progress)

    def login(self):
        """
        just return progress and settings in case of login
        :return:
        """
        pass

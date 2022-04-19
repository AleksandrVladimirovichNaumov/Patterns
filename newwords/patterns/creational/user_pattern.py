"""module with user pattern based on prototype pattern"""
import copy
import hashlib


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
        self.topics_progress = [[0 for i in range(topic_qnty)] for m in range(language_qnty)]

    def generate_subtopic_progress(self, language_qnty, topic_qnty, subtopic_qnty):
        """
        generating initial list with percentage for each subtopic progress
        :param language_qnty:
        :param topic_qnty:
        :param subtopic_qnty:
        :return:
        """
        self.subtopics_progress = [[[0 for i in range(subtopic_qnty)] for n in range(topic_qnty)] for m in
                                   range(language_qnty)]

    def set_settings(self, dict_obj):
        """
        settings stored in dict obj. method adds or replace settings
        :param dict_obj:
        :return:
        """
        self.settings |= dict_obj

    def register(self, email, password_1, password_2):
        """
        creating duplicate of a user with registration details
        :param settings: settings of user
        :param email: email from form
        :param password: pass from form
        :return: copy of user instance
        """
        self.email = email
        # email is a salt for password's hash
        self.password = hashlib.sha256(bytes(password_1) + bytes(email))
        return copy.deepcopy(self)

    def login(self):
        """
        just return progress and settings in case of login
        :return:
        """
        pass


class SessionUser(User):
    """
    progress for this type of user is kept on a server
    session user is a prototype for this class
    """
    pass

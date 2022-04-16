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
        # which languages are selected
        self.settings = {}
        # topics progress
        self.topics_progress = {}
        # subtopic progress
        self.subtopics_progress = {}
        # personal info
        self.email = ''
        self.password = ''

    def register(self, email, password, settings, topics_progress, subtopics_progress):
        """
        creating duplicate of a user with registration details
        :param settings: settings of user
        :param email: email from form
        :param password: pass from form
        :return: copy of user instance
        """
        self.email = email
        # email is a salt for password's hash
        self.password = hashlib.sha256(bytes(password) + bytes(email))
        self.settings = settings
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

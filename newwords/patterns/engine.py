"""module with main interface. Facade pattern was used"""
import hashlib
import json

from patterns.creational.database_pattern import NewWordsStorage
from patterns.creational.settings_pattern import SettingBuilder
from patterns.creational.user_pattern import User
from patterns.structural.decorators_patterns import LoginCheck, Debug


class Engine(NewWordsStorage):
    """
    main interface of a NewWord project
    """

    def __init__(self):
        # self.database = NewWordsStorage()
        super().__init__()
        # creating session user and set default settings
        self.user = User().generate_settings(SettingBuilder().set_main_language(1).set_second_language(2).build())
        # creating languages list
        self.languages = self.get_languages()
        # creating topic list
        self.topics = self.get_topics(self.user.get_main_language())
        # creating subtopic list
        self.subtopics = self.get_subtopics(self.user.get_main_language(), len(self.topics))
        # generating progress for session user
        self.user \
            .generate_topic_progress(len(self.languages), len(self.topics)) \
            .generate_subtopic_progress(len(self.languages), len(self.topics), len(self.subtopics[1]))

    # User methods

    @LoginCheck
    def set_setting(self, key, value):
        self.user.settings[key] = value
        if self.user.registered:
            self.database_set_setting(self.user.email, self.user.settings)

    def get_settings(self):
        return self.user.settings

    def register_user(self, email, password_1):
        return self.add_user(*self.user.data_to_register(email, password_1))

    def login(self, email, password):
        if not self.user.registered:
            login_result = self.database_login(email, hashlib.sha256(bytes(password, 'utf-8')+bytes(email, 'utf-8')).hexdigest())
            if login_result is not False:
                self.user.username = login_result[0]
                self.user.email = login_result[1]
                self.user.settings = json.loads(login_result[2])
                self.user.topics_progress = json.loads(login_result[3])
                self.user.subtopics_progress = json.loads(login_result[4])
                self.user.registered = True
                print("login successfully")

    def get_topics_progress(self):
        return self.user.topics_progress

    def get_subtopics_progress(self):
        return self.user.subtopics_progress

    def get_username(self):
        return self.user.username

    def get_user_data(self):
        return {'is_registered': self.user.registered,
                'username': self.user.username}

    @staticmethod
    def get_main_words():
        # temporary. will be taken from database
        return ['word 1', 'word 2', 'word 3', 'word 4', 'word 5', 'word 6', 'word 7', 'word 8', 'word 9', 'word 10']

    @staticmethod
    def get_second_words():
        # temporary. will be taken from database
        return ['word 1', 'word 2', 'word 3', 'word 4', 'word 5', 'word 6', 'word 7', 'word 8', 'word 9', 'word 10']

    @staticmethod
    def get_content_words(language):
        pass

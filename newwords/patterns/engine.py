"""module with main interface. Facade pattern was used"""
from patterns.creational.database_pattern import NewWordsStorage
from patterns.creational.settings_pattern import SettingBuilder
from patterns.creational.user_pattern import SessionUser
from patterns.structural.decorators_patterns import LoginCheck, Debug



class Engine:
    """
    main interface of a NewWord project
    """

    def __init__(self):
        self.user = SessionUser()
        self.settings = SettingBuilder().set_main_language(1).set_second_language(2)
        self.database = NewWordsStorage()

    @LoginCheck
    def set_settings(self, key, value):
        if key == 'main_language':
            self.settings.set_main_language(value)
        elif key == 'second_language':
            self.settings.set_second_language(value)

    def get_settings(self):
        return self.settings.build()

    def register_user(self, username, email, password_1, password_2, settings, topics_progress, subtopics_progress):
        return self.user.register(username, email, password_1, password_2, settings, topics_progress, subtopics_progress)

    def get_languages(self):
        return self.database.get_languages()

    def get_topics_progress(self):
        return self.user.topics_progress

    def get_subtopics_progress(self):
        return self.user.subtopics_progress

    def get_usernmae(self):
        return self.user.username

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

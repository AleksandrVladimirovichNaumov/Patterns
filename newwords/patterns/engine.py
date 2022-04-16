"""module with main interface"""
from patterns.creational.settings_pattern import SettingBuilder
from patterns.creational.user_pattern import SessionUser
from temp_storage import LANGUAGES, TOPICS, SUBTOPICS


class Engine:
    """
    main interface of a NewWord project
    """

    def __init__(self):
        self.user = SessionUser()
        self.settings = SettingBuilder().set_main_language(1).set_second_language(2)

    def set_settings(self, key, value):
        if key == 'main_language':
            self.settings.set_main_language(value)
        elif key == 'second_language':
            self.settings.set_second_language(value)

    def get_settings(self):
        return self.settings.build()

    def register_user(self, email, password, settings, topics_progress, subtopics_progress):
        return self.user.register(email, password, settings, topics_progress, subtopics_progress)

    @staticmethod
    def get_languages():
        return LANGUAGES

    @staticmethod
    def get_topics(language_index):
        return TOPICS[language_index]

    @staticmethod
    def get_subtopics(language_index, topic):
        return SUBTOPICS[language_index][TOPICS.index(topic)]

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


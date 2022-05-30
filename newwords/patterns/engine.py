"""module with main interface. Facade pattern was used"""
import hashlib
import json
import sqlite3

from patterns.creational.database_pattern import NewWordsStorage
from patterns.creational.settings_pattern import SettingBuilder
from patterns.creational.user_pattern import User
from patterns.structural.decorators_patterns import LoginCheck
from patterns.architectual.translation_pattern import TranslationMapper


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
            .generate_subtopic_progress(len(self.languages), len(self.topics), len(self.subtopics[0]))
        # current topic & subtopic to save progress
        self.current_topic = 0
        self.current_subtopic = 0
        # separate pattern to work with page content translation

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
                self.user.subtopics_progress = json.loads(login_result[3])
                self.user.topics_progress = self.user.calculate_topic_progress(len(self.languages))
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
                'username': self.user.username,
                'topic_progress': self.user.topics_progress,
                'subtopic_progress': self.user.subtopics_progress}

    def get_json_topic_progress(self):
        return json.dumps(self.user.topics_progress)

    def get_json_subtopic_progress(self):
        return json.dumps(self.user.subtopics_progress)

    def get_app_words(self, topic_number, subtopic_number):
        return [self.get_words(self.get_settings()['main_language'], topic_number, subtopic_number),
                self.get_words(self.get_settings()['second_language'], topic_number, subtopic_number)]

    def set_topic_progress(self, value):
        self.user.topics_progress[self.user.get_main_language()][self.user.get_second_language()][self.current_topic] = value

    def set_subtopic_progress(self, value):
        self.user.subtopics_progress[self.user.get_main_language()][self.user.get_second_language()][self.current_topic][self.current_subtopic] = value
        if self.user.registered:
            self.database_set_progress(self.user.email, self.user.subtopics_progress)


    def update_topic_progress(self):
        subtopic_progress = self.user.subtopics_progress[self.user.get_main_language()][self.user.get_second_language()][self.current_topic]
        self.user.topics_progress[self.user.get_main_language()][self.user.get_second_language()][self.current_topic] = int(sum(subtopic_progress)/len(subtopic_progress))


    @staticmethod
    def get_content_words(language):
        pass

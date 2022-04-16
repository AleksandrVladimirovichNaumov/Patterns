"""module for settings patterns based on builder pattern"""


class SettingBuilder:
    def __init__(self):
        self.settings = {}

    def set_main_language(self, main_language):
        self.settings['main_language'] = main_language
        return self

    def set_second_language(self, main_language):
        self.settings['second_language'] = main_language
        return self

    def build(self):
        return self.settings

    # getters

    def get_main_language(self):
        return self.settings.get('main_language')

    def get_second_language(self):
        return self.settings.get('second_language')


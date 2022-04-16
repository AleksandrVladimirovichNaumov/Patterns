"""module for settings patterns based on builder pattern"""


class SettingBuilder:
    def __init__(self):
        self.settings = SettingBuilder()

    def set_main_language(self, main_language):
        self.settings._dict['main_language'] = main_language

    def set_second_language(self, main_language):
        self.settings._dict['second_language'] = main_language

    def build(self):
        return self.settings

    # getters

    def get_main_language(self):
        return self.settings._dict.get('main_language')

    def get_second_language(self):
        return self.settings._dict.get('second_language')


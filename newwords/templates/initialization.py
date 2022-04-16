from patterns.creational.settings_pattern import SettingBuilder
from temp_storage import LANGUAGES

USER_SETTING = SettingBuilder().set_main_language(LANGUAGES[0]).set_second_language(LANGUAGES[1])

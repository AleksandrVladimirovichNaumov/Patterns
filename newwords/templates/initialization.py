from patterns.creational.settings_pattern import SettingBuilder
from temp_storage import LANGUAGES


def setting_initialize():
    """
    get user settings from database. if no settings - apply default
    :return: -
    """
    user_settings = SettingBuilder().set_main_language(LANGUAGES[0]).set_second_language(LANGUAGES[1])
    print(user_settings.build())
    return user_settings.build()

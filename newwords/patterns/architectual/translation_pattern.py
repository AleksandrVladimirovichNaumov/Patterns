"""module for translation of page content based on a mapper pattern"""
import sqlite3

from temp_storage import TRANSLATION


class TranslatedWord:
    """model of translated word"""

    def __init__(self, language_number, word_number, word):
        self.id = None
        self.language_number = language_number
        self.word_number = word_number
        self.word = word


class TranslationMapper:
    """
     DATA MAPPER pattern
    """

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def find_word(self, language_number, word_number):
        statement = "SELECT WORD FROM CONTENT_TRANSLATION WHERE LANGUAGE_NUMBER =? AND WORD_NUMBER =?"
        self.cursor.execute(statement, (language_number, word_number,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            raise Exception(f'record with id={word_number} not found')

    def get_words_list(self, language_number):
        statement = "SELECT WORD FROM CONTENT_TRANSLATION WHERE LANGUAGE_NUMBER =? ORDER BY WORD_NUMBER"
        self.cursor.execute(statement, (language_number,))
        result = self.cursor
        if result:
            return [i[0] for i in result]
        else:
            raise Exception(f'no words found')

    def _add_word(self, language_number, word_number, word):
        statement = "INSERT INTO CONTENT_TRANSLATION (LANGUAGE_NUMBER, WORD_NUMBER, WORD) VALUES (?, ?, ?)"
        self.cursor.execute(statement, (language_number, word_number, word))
        try:
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print(e)

    def _update_word(self, language_number, word_number, word):
        statement = "UPDATE CONTENT_TRANSLATION SET WORD=? WHERE LANGUAGE_NUMBER =? AND WORD_NUMBER =?"

        self.cursor.execute(statement, (language_number, word_number, word))
        try:
            self.connection.commit()
        except Exception as e:
            print(e)

    def _delete(self, language_number, word_number):
        statement = "DELETE FROM CONTENT_TRANSLATION WHERE LANGUAGE_NUMBER =? AND WORD_NUMBER =?"

        self.cursor.execute(statement, (language_number, word_number))
        try:
            self.connection.commit()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    connection = sqlite3.connect('../creational/db_newwords.db3')
    translation_mapper = TranslationMapper(connection)
    for word_number, words in enumerate(TRANSLATION):
        for language_number, word in enumerate(words):
            translation_mapper._add_word(language_number, word_number, word)
            print(f'translation {word} was added')
    # print(translation_mapper.find_word(0,0))
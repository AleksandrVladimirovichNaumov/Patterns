import os

from sqlalchemy import __version__, create_engine, Table, Column, MetaData, \
    Integer, String, DateTime, ForeignKey, JSON, Text
from sqlalchemy.orm import mapper, sessionmaker

from temp_storage import LANGUAGES, TOPICS, SUBTOPICS, WORDS


class SingConnection(type):
    """
    Singleton pattern is used to confirm that there is only 1 connection to database
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class NewWordsStorage(metaclass=SingConnection):
    print(f"Version of SQLAlchemy: {__version__}")

    class Users:
        """
        table with users
        """

        def __init__(self, email, password, settings, progress):
            self.id = None
            self.email = email
            self.password = password
            self.settings = settings
            self.progress = progress

    class Languages:
        """
        table with languages
        """

        def __init__(self, language, number):
            self.id = None
            self.language = language
            self.number = number

    class Topics:
        """
        table with topics
        """

        def __init__(self, language_id, topic, number):
            self.id = None
            self.language_id = language_id
            self.topic = topic
            self.number = number

    class SubTopics:
        """
        table with subtopics
        """

        def __init__(self, topic_id, subtopic, number):
            self.id = None
            self.topic_id = topic_id
            self.subtopic = subtopic
            self.number = number

    class Words:
        """
        table with words
        """

        def __init__(self, subtopic_id, word_1, word_2, word_3, word_4, word_5, word_6, word_7, word_8, word_9,
                     word_10):
            self.id = None
            self.subtopic_id = subtopic_id
            self.word_1 = word_1
            self.word_2 = word_2
            self.word_3 = word_3
            self.word_4 = word_4
            self.word_5 = word_5
            self.word_6 = word_6
            self.word_7 = word_7
            self.word_8 = word_8
            self.word_9 = word_9
            self.word_10 = word_10

    def __init__(self):
        # each client will have local db
        path = os.path.dirname(os.path.realpath(__file__))
        filename = 'db_newwords.db3'
        self.engine = create_engine(f'sqlite:///{os.path.join(path, filename)}',
                                    echo=False,
                                    pool_recycle=7200,
                                    connect_args={'check_same_thread': False})
        # create metadata
        self.metadata = MetaData()

        # table with users
        self.users_table = Table('Users',
                                 self.metadata,
                                 Column('id', Integer, primary_key=True),
                                 Column('email', String, unique=True),
                                 Column('passwords', String),
                                 Column('registered', DateTime),
                                 Column('settings', JSON),
                                 Column('progress', JSON)),

        # table with languages
        self.languages_table = Table('Languages',
                                     self.metadata,
                                     Column('id', Integer, primary_key=True),
                                     Column('language', String),
                                     Column('number', Integer, unique=True)),

        # table with topics
        self.topics_table = Table('Topics',
                                  self.metadata,
                                  Column('id', Integer, primary_key=True),
                                  Column('language_id', ForeignKey('Languages.id')),
                                  Column('topic', String),
                                  Column('number', Integer)),
        # table with subtopics
        self.subtopics_table = Table('SubTopics',
                                     self.metadata,
                                     Column('id', Integer, primary_key=True),
                                     Column('topic_id', ForeignKey('Topics.id')),
                                     Column('subtopic', String),
                                     Column('number', Integer)),

        # table with words
        self.words_table = Table('Words',
                                 self.metadata,
                                 Column('id', Integer, primary_key=True),
                                 Column('subtopic_id', ForeignKey('SubTopics.id')),
                                 Column('word_1', String),
                                 Column('word_2', String),
                                 Column('word_3', String),
                                 Column('word_4', String),
                                 Column('word_5', String),
                                 Column('word_6', String),
                                 Column('word_7', String),
                                 Column('word_8', String),
                                 Column('word_9', String),
                                 Column('word_10', String)
                                 ),

        # create tables
        self.metadata.create_all(self.engine)
        # connect classes with tables
        mapper(self.Users, self.users_table[0])
        mapper(self.Languages, self.languages_table[0])
        mapper(self.Topics, self.topics_table[0])
        mapper(self.SubTopics, self.subtopics_table[0])
        mapper(self.Words, self.words_table[0])

        # create session
        server_session = sessionmaker(bind=self.engine)
        self.session = server_session()
        # # saves all changes
        # self.session.commit()

    def get_settings(self, email):
        """
        get setting based on user email
        :param email: users email
        :return: json with settings
        """
        query = self.session.query(self.Users.settings).filter_by(email=email).first()
        return query

    def _add_language(self, language, number):
        """
        add language to db
        :param language:
        :param number:
        :return: -
        """
        try:
            new_language = self.Languages(language, number)
            self.session.add(new_language)
            self.session.commit()
            print(f'language "{language}" was added')
        except Exception as exception:
            self.session.rollback()
            print(exception)

    def _add_topic(self, language_number, topic, number):
        """
        add topic to db
        :param language_number:
        :param topic:
        :param number:
        :return:
        """
        try:
            language_id = self.session.query(self.Languages.id).filter_by(number=language_number).first().id
            new_topic = self.Topics(language_id, topic, number)
            self.session.add(new_topic)
            self.session.commit()
            print(f'topic "{topic}" was added')
        except Exception as exception:
            self.session.rollback()
            print(exception)

    def _add_subtopic(self, language_number, topic_number, subtopic, number):
        """
        add subtopic to db
        :param language_number:
        :param topic_number:
        :param subtopic:
        :param number:
        :return:
        """
        try:
            language_id = self.session.query(self.Languages.id).filter_by(number=language_number).first().id
            topic_id = self.session.query(self.Topics.id).filter_by(number=topic_number,
                                                                    language_id=language_id).first().id
            new_subtopic = self.SubTopics(topic_id, subtopic, number)
            self.session.add(new_subtopic)
            self.session.commit()
            print(f'subtopic "{subtopic}" was added')
        except Exception as exception:
            self.session.rollback()
            print(exception)

    def _add_words(self, language_number, topic_number, subtopic_number, words):
        """
        add words to db
        :param language_number:
        :param topic_number:
        :param subtopic_number:
        :param words:
        :return:
        """
        try:
            language_id = self.session.query(self.Languages.id).filter_by(number=language_number).first().id
            topic_id = self.session.query(self.Topics.id).filter_by(number=topic_number,
                                                                    language_id=language_id).first().id
            subtopic_id = self.session.query(self.SubTopics.id).filter_by(number=subtopic_number,
                                                                          topic_id=topic_id).first().id
            new_words = self.Words(subtopic_id, *words)
            self.session.add(new_words)
            self.session.commit()
            print(f'words {words} were added')
        except Exception as exception:
            self.session.rollback()
            print(exception)


if __name__ == '__main__':
    test_db = NewWordsStorage()
    # add languages
    for number, language in enumerate(LANGUAGES):
        test_db._add_language(language, number)

    # add topics
    for language_number, topics in enumerate(TOPICS):
        for number, topic in enumerate(topics):
            test_db._add_topic(language_number, topic, number)

    # add subtopics
    for language_number, topics in enumerate(SUBTOPICS):
        for topic_number, subtopics in enumerate(topics):
            for number, subtopic in enumerate(subtopics):
                test_db._add_subtopic(language_number, topic_number, subtopic, number)

    # add words
    for language_number in range(4):
        for topic_number in range(10):
            for subtopic_number in range(9):
                test_db._add_words(language_number, topic_number, subtopic_number, WORDS)
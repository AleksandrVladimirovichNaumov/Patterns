






class Engine:
    """
    main interface of a NewWord project
    """

    def __int__(self):
        self.users = []
        self.languages = []
        self.topics = []
        self.subtopics = []
        self.words = []

    @staticmethod
    def create_user():
        pass

    @staticmethod
    def get_languages():
        pass

    @staticmethod
    def get_topics(language):
        pass

    @staticmethod
    def get_subtopics(language):
        pass

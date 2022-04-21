import abc


# topic classes

class TopicGet(metaclass=abc.ABCMeta):

    def get_items(self):
        pass


class TopicUpdate(metaclass=abc.ABCMeta):

    def update_items(self):
        pass


# subtopic classes

class SubTopicGet(metaclass=abc.ABCMeta):

    def get_items(self):
        pass


class SubTopicUpdate(metaclass=abc.ABCMeta):

    def update_items(self):
        pass


# abstract factory

class AbstractFactory(abc.ABC):

    @staticmethod
    def create_factory(name):
        PROGRESS = {
            'topic': TopicFactory,
            'subtopic': SubTopicFactory,
        }
        return PROGRESS[name]()

    @abc.abstractmethod
    def get_items(self):
        pass

    @abc.abstractmethod
    def update_items(self):
        pass


# progress & settings factory

class TopicFactory(AbstractFactory):

    def get_items(self):
        return TopicGet()

    def update_items(self):
        return TopicUpdate()


class SubTopicFactory(AbstractFactory):

    def get_items(self):
        return SubTopicGet()

    def update_items(self):
        return SubTopicUpdate()


class SettingsFactory(AbstractFactory):

    def get_items(self):
        return SettingsGet()

    def update_items(self):
        return SettingsUpdate()

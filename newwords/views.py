"""Module with all views"""
from chillout_framework.templater import Templater
from patterns.structural.decorators_patterns import Debug



class Index(Templater):
    """
    view for index page
    """

    def __init__(self, **kwargs):
        self.template = 'index.html'
        self.folder = 'templates'
        self.route = '/'
        super().__init__(self.template, self.folder, **kwargs)

    @Debug
    def __call__(self, request):
        return '200 OK', self.render(
            topics=request.get('topics', None),
            style=request.get('style', None),
            languages=request.get('languages', None),
            settings=request.get('settings', None)
        )



class MobileApplication(Templater):
    """
    view for mobile application page
    """

    def __init__(self, **kwargs):
        self.template = 'mobile_application.html'
        self.folder = 'templates'
        self.route = '/mobile_application/'
        super().__init__(self.template, self.folder, **kwargs)

    @Debug
    def __call__(self, request):
        return '200 OK', self.render(
            topics=request.get('topics', None),
            style=request.get('style', None),
            languages=request.get('languages', None),
            settings=request.get('settings', None)
        )



class NotFound404:
    """
    view for 404 page
    """

    def __init__(self):
        self.template = 'base.html'
        self.folder = 'templates'
        self.route = '/404/'

    @Debug
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


class Login(Templater):
    """
    view login page
    """

    def __init__(self):
        self.template = 'login.html'
        self.folder = 'templates'
        self.route = '/login/'

    @Debug
    def __call__(self, request):
        return '200 OK', self.render(
            topics=request.get('topics', None),
            style=request.get('style', None),
            languages=request.get('languages', None),
            settings=request.get('settings', None)
        )



class Registration(Templater):
    """
    view login page
    """

    def __init__(self):
        self.template = 'registration.html'
        self.folder = 'templates'
        self.route = '/registration/'

    @Debug
    def __call__(self, request):
        return '200 OK', self.render(
            topics=request.get('topics', None),
            style=request.get('style', None),
            languages=request.get('languages', None),
            settings=request.get('settings', None)
        )



class App(Templater):
    """
    view application page
    """

    def __init__(self):
        self.template = 'app.html'
        self.folder = 'templates'
        self.route = '/application/'
    @Debug
    def __call__(self, request):
        return '200 OK', self.render(
            topics=request.get('topics', None),
            style=request.get('style', None),
            words=request.get('words', None),
            languages=request.get('languages', None),
            settings=request.get('settings', None)
        )

"""Module with all views"""
from engine.templater import Templater


class Index(Templater):
    """
    view for index page
    """

    def __init__(self, **kwargs):
        self.template = 'index.html'
        self.folder = 'templates'
        self.route = '/'
        super().__init__(self.template, self.folder, **kwargs)

    def __call__(self, request):
        return '200 OK', self.render(
            topics=request.get('topics', None),
            style=request.get('style', None),
            languages=request.get('languages', None)
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

    def __call__(self, request):
        return '200 OK', self.render(
            topics=request.get('topics', None),
            style=request.get('style', None),
            languages=request.get('languages', None)
        )


class NotFound404:
    """
    view for 404 page
    """

    def __init__(self):
        self.template = 'base.html'
        self.folder = 'templates'
        self.route = '/404/'

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

    def __call__(self, request):
        return '404 WHAT', self.render(
            topics=request.get('topics', None),
            style=request.get('style', None),
            languages=request.get('languages', None)
        )


class Registration(Templater):
    """
    view login page
    """

    def __init__(self):
        self.template = 'registration.html'
        self.folder = 'templates'
        self.route = '/registration/'

    def __call__(self, request):
        return '404 WHAT', self.render(
            topics=request.get('topics', None),
            style=request.get('style', None),
            languages=request.get('languages', None)
        )

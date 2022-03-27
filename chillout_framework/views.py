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
        print(request)
        return '200 OK', self.render(response=request.get('topics', None))


class About(Templater):
    """
    view for about page
    """
    def __init__(self, **kwargs):
        self.template = 'index.html'
        self.folder = 'templates'
        self.route = '/about/'
        super().__init__(self.template, self.folder, **kwargs)

    def __call__(self, request):
        return '200 OK', 'about'


class NotFound404:
    """
    view for 404 page
    """
    def __init__(self):
        self.template = 'index.html'
        self.folder = 'templates'
        self.route = '/404/'

    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'

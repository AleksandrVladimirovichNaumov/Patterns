from engine.templater import Templater


class Index(Templater):
    def __init__(self, **kwargs):
        self.template = 'index.html'
        self.folder = 'templates'
        self.route = '/'
        super().__init__(self.template, self.folder, **kwargs)

    def __call__(self, request):
        print(request)
        return '200 OK', self.render(data=request.get('data', None))


class About(Templater):
    def __init__(self, **kwargs):
        self.template = 'index.html'
        self.folder = 'templates'
        self.route = '/about/'
        super().__init__(self.template, self.folder, **kwargs)

    def __call__(self, request):
        return '200 OK', 'about'



class NotFound404:

    def __init__(self):
        self.template = 'index.html'
        self.folder = 'templates'
        self.route = '/404/'

    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'

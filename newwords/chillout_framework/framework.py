"""main module of framework"""
import inspect
from controllers import Controllers
import views
from newwords.chillout_framework.requests import ChillOutRequests
from views import NotFound404


class ChillOutFramework(ChillOutRequests):
    """
    main class to run framework
    """

    def __init__(self):
        # list of controllers for frontend requests
        self.frontend = [method[1] for method in
                         inspect.getmembers(Controllers, predicate=inspect.isfunction)]
        # list of available routes
        self.routes = {}
        # dict with all requests
        self.requests = {}
        # make dict {route:view}
        # scanning view.py for all classes
        # class = view except Templator (parent of view) and Engine
        # checking that name of class is not 'Templater' because it is not a view
        for class_obj in inspect.getmembers(views, predicate=inspect.isclass):
            if not class_obj[0] == 'Templater' and not class_obj[0] == 'Debug':
                self.routes[class_obj[1]().route] = class_obj[1]()

    def __call__(self, environ, start_response):
        """
        :param environ: dict from server
        :param start_response: function to response to server
        :return:
        """
        # take path of address
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        # take a view based on a path
        view = self.routes[path] if path in self.routes else NotFound404()

        # get data from request
        method = environ['REQUEST_METHOD']
        self.requests['method'] = method

        if method == 'POST':
            data = self.get_post_requests(environ)
            self.requests['POST_DATA'] = data

        if method == 'GET':
            request_params = self.get_get_requests(environ)
            self.requests['GET_DATA'] = request_params

        # find required controller to maintain frontend request
        for controller in self.frontend:
            controller(self.requests)

        # get code and content from view
        code, content = view(self.requests)
        start_response(code, [('Content-Type', 'text/html')])
        return [content.encode('utf-8')]

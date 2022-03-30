"""main module of framework"""
import inspect
from controllers import Controllers
import views
from views import NotFound404


class ChillOutFramework:
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
        # class = view except Templator (parent of view)
        # checking that name of class is not 'Templater' because it is not a view
        for class_obj in inspect.getmembers(views, predicate=inspect.isclass):
            if not class_obj[0] == 'Templater':
                self.routes[class_obj[1]().route] = class_obj[1]()

    def __call__(self, environ, start_response):
        """
        :param environ: dict from server
        :param start_response: function to response to server
        :return:
        """
        print(environ)
        # take path of address
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        # take a view based on a path
        view = self.routes[path] if path in self.routes else NotFound404()

        # printing get and post if exist
        self.get_requests(environ)
        # find required controller to maintain frontend request
        for controller in self.frontend:
            controller(self.requests)

        # get code and content from view
        code, content = view(self.requests)
        start_response(code, [('Content-Type', 'text/html')])
        return [content.encode('utf-8')]

    @staticmethod
    def parse_query(query):
        """
        parse query from server to dict
        :param query: query from server
        :return: dict based on query
        """
        dict_obj = {}
        if query:
            # parameters = ((item.split('=')) for item in query.split('&'))
            # dict_obj = {key: value for key, value in parameters}
            dict_obj = {item.split('=')[0]: item.split('=')[1] for item in query.split('&')}
        return dict_obj

    def get_requests(self, environ):
        """
        get requests from server
        :param environ:
        :return: get, post
        """
        # getting get request
        get = self.parse_query(environ["QUERY_STRING"])
        print(f'get request(s): {get}')

        # getting post request
        # dict for post
        post = {}
        # getting length of post if exist
        content_length = int(environ.get('CONTENT_LENGTH')) if environ.get('CONTENT_LENGTH') else 0

        # read bytes from post request
        post_bytes = environ.get('wsgi.input').read(content_length) if content_length > 0 else b''

        # bytes to dict for post
        if post_bytes:
            # decoding
            post_str = post_bytes.decode(encoding='utf-8')
            # put in dict
            post = self.parse_query(post_str)
        print(f'post request(s): {post}')
        return get, post

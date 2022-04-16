""" module for class to work with get and post requests"""


class ChillOutRequests:
    """
    main class to work with post and get requests
    """

    @staticmethod
    def parse_query(query):
        """
        parse query from server to dict
        :param query: query from server
        :return: dict based on query
        """
        dict_obj = {}
        if query:
            dict_obj = {item.split('=')[0]: item.split('=')[1] for item in query.split('&')}
        return dict_obj

    def get_get_requests(self, environ):
        """
        get get requests
        :param environ:
        :return: get request
        """

        # getting get request
        get = self.parse_query(environ["QUERY_STRING"])
        print(f'get request(s): {get}')
        return get

    def get_post_requests(self, environ):
        """
        get post requests
        :param environ:
        :return: post request
        """

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
        return post


    # def request_service(self, dict_obj):
    #     if dict_obj["REQUEST_METHOD"] == 'GET':
    #         if self.get_get_requests().get('main_language')is not None:
    #             self

"""module with commands for server"""
import urllib.parse
from wsgiref.simple_server import make_server
from chillout_framework.framework import ChillOutFramework
from chillout_framework.settings import HOST, PORT

server = ChillOutFramework()

def start():
    """
    function to start a server
    :return: -
    """
    with make_server(HOST, PORT, server) as httpd:
        print("ChillOut server is starting")
        # link with ip of a server
        link = urllib.parse.quote(HOST)
        print(f'http://{link}:{PORT}/')
        # starting a server
        httpd.serve_forever()


if __name__ == '__main__':
    start()

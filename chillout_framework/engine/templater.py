"""Render class"""
import os.path
from jinja2 import Template, Environment, FileSystemLoader


class Templater:
    """
    class to work with templates
    """

    def __init__(self, template, folder, **kwargs):
        self.template = template
        self.folder = folder

    def render(self, **kwargs):
        """
        render template of class object
        :return: render of template
        """
        # path to template
        # path = os.path.join(self.folder, self.template)

        env = Environment()
        env.loader = FileSystemLoader(self.folder)
        template = env.get_template(self.template)

        # read full template
        # with open(path, encoding='utf-8') as file:
        #     template = Template(file.read())
        return template.render(**kwargs)

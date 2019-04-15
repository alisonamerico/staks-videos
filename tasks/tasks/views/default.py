from pyramid.view import view_config


class TaskView(object):
    def __init__(self, request):
        self.request = request
        self.view_name = 'TaskView'

    @view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
    def home(self):
        return {'tasks': 'tasks'}

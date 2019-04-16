from pyramid.view import view_config
from tasks.models import Task


class TaskView(object):
    def __init__(self, request):
        self.request = request
        self.view_name = 'TaskView'

    @view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
    def home(self):
        tasks = Task.objects.first()
        return {'tasks': tasks}

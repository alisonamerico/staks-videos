"""
Imports
"""

import os
import logging
import sqlite3

from pyramid.config import Configurator
from pyramid.events import ApplicationCreated
from pyramid.events import NewRequest
from pyramid.events import subscriber
from pyramid.session import UnencryptedCookieSessionFactoryConfig

from wsgiref.simple_server import make_server

"""
Configures the logging and the current working directory path
"""
logging.basicConfig()
log = logging.getLogger(__file__)

here = os.path.dirname(os.path.abspath(__file__))


@subscriber(NewRequest)
def new_request_subscriber(event):
    request = event.request
    settings = request.registry.settings
    request.db = sqlite3.connect(settings['db'])
    request.add_finished_callback(close_db_connection)


def close_db_connection(request):
    request.db.close()


@subscriber(ApplicationCreated)
def application_created_subscriber(event):
    log.warning('Initializing database...')
    with open(os.path.join(here, 'schema.sql')) as f:
        stmt = f.read()
        settings = event.app.registry.settings
        db = sqlite3.connect(settings['db'])
        db.executescript(stmt)
        db.commit()


"""
Configure the Pyramid application, establishing rudimentary sessions,
we will get the WSGI application to run the local server.
"""

if __name__ == '__main__':
    # configuration settings
    settings = {}
    settings['reload_all'] = True
    settings['debug_all'] = True
    settings['db'] = os.path.join(here, 'tasks.db')
    # session factory
    session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    # configuration setup
    config = Configurator(settings=settings, session_factory=session_factory)
    # scan for @view_config and @subscriber decorators
    config.scan()
    # serve app
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

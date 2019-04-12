"""
Imports
"""

import os
import logging

from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig

from wsgiref.simple_server import make_server

"""
Configures the logging and the current working directory path
"""
logging.basicConfig()
log = logging.getLogger(__file__)

here = os.path.dirname(os.path.abspath(__file__))


"""
Configure the Pyramid application, establishing rudimentary sessions,
we will get the WSGI application to run the local server.
"""
if __name__ == '__main__':
    # configuration settings
    settings = {}
    settings['reload_all'] = True
    settings['debug_all'] = True
    # session factory
    session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    # configuration setup
    config = Configurator(settings=settings, session_factory=session_factory)
    # serve app
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

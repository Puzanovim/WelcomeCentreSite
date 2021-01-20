from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid_sqlalchemy import BaseObject, Session
from wsgiref.simple_server import make_server


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # db
    # engine = engine_from_config(settings, 'sqlalchemy.')
    # Session.configure(bind=engine)
    # BaseObject.metadata.bind = engine
    # settings
    config = Configurator(settings=settings)
    config.include('pyramid_sqlalchemy')
    config.include('pyramid_debugtoolbar')
    config.include('pyramid_tm')
    # routes
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('main', '/')
    config.add_route('events', '/events')
    config.add_route('projects', '/projects')
    config.add_route('event', '/events/{id}')
    config.add_route('project', '/projects/{id}')
    config.add_route('order', '/orders/{id}')
    config.add_route('new_order', '/new_order')

    config.scan()
    return config.make_wsgi_app()

from pyramid.config import Configurator
from .views import not_found


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # settings
    config = Configurator(settings=settings)
    config.include('pyramid_sqlalchemy')
    config.include('pyramid_debugtoolbar')
    config.include('pyramid_tm')
    # routes
    config.add_static_view(name='static', path='WelcomeCentreSite:static')
    config.add_route('main', '/')
    config.add_route('events', '/events')
    config.add_route('projects', '/projects')
    config.add_route('event', '/events/{id}')
    config.add_route('project', '/projects/{id}')
    config.add_route('order', '/orders/{id}')
    config.add_route('new_order', '/new_order')
    config.add_route('404', '/page_not_found')
    config.add_notfound_view(not_found)

    config.scan()
    return config.make_wsgi_app()

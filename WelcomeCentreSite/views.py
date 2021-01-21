from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid_sqlalchemy import Session
import datetime

from .models import Event, Project, Order


@view_config(route_name="main", renderer="templates/index.jinja2")
def index_page(request):
    """
    Главная страница
    """
    title = "Welcome Centre"
    return {'title': title}


@view_config(route_name="events", renderer="templates/events.jinja2")
def events_page(request):
    """
    Страница мероприятий
    """
    title = "Мероприятия"
    events_info = Event.get_events()
    return {'title': title, 'events': events_info}


@view_config(route_name="projects", renderer="templates/projects.jinja2")
def projects_page(request):
    """
    Страница проектов
    """
    title = "Проекты"
    projects_info = Project.get_projects()
    return {'title': title, 'projects': projects_info}


@view_config(route_name="event", renderer="templates/event.jinja2")
def event_page(request):
    """
    Информация о мероприятии по id
    """
    title = "Мероприятие"
    event_id = request.matchdict['id']
    event_info = Event.get_event_info(event_id)
    return {'title': title, 'info': event_info}


@view_config(route_name="project", renderer="templates/project.jinja2")
def project_page(request):
    """
    Информация о проекте по id
    """
    title = "Проект"
    project_id = request.matchdict['id']
    project_info = Project.get_project_info(project_id)
    return {'title': title, 'info': project_info}


@view_config(route_name="order", renderer="templates/order.jinja2")
def order_page(request):
    """
    Информация о заказе по id
    """
    title = "Заказ"
    order_id = request.matchdict['id']
    order_info = Order.get_order_info(order_id)
    return {'title': title, 'info': order_info}


@view_config(route_name="new_order", renderer="templates/new_order.jinja2")
def add_order(request):
    """
    Форма заказа
    """
    if 'form.submitted' in request.params:
        date = request.params['date']
        date = date.split("-")
        time = request.params['time']
        time = time.split(":")
        order = Order(name=request.params['name'],
                      phone=request.params['phone'],
                      email=request.params['email'],
                      contact_face=request.params['contact_face'],
                      event=int(request.params['event']),
                      date=datetime.date(year=int(date[0]),
                                         month=int(date[1]),
                                         day=int(date[2])),
                      time=datetime.time(hour=int(time[0]),
                                         minute=int(time[1])),
                      address=request.params['address'],
                      count_participants=int(request.params['count_participants']),
                      note=request.params['note'])
        Session.add(order)
        current_order_id = Order.get_last_order().id
        next_url = request.route_url('order', id=current_order_id)
        return HTTPFound(location=next_url)
    return {
        "title": "Добавление новой записи",
        "save_url": request.route_url('new_order'),
        "events": Event.get_events()
    }

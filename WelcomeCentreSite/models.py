from pyramid_sqlalchemy import BaseObject, Session
from sqlalchemy import Column, Date, Time, \
    Integer, Unicode, UnicodeText, ForeignKey, String


class Event(BaseObject):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(UnicodeText, default=u'Нет данных')
    promo = Column(String, default="Нет данных")
    cost = Column(Integer, default=0)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    contact_face = Column(String, nullable=False)
    promo_img = Column(String, nullable=True)

    @classmethod
    def get_event_info(cls, event_id):
        return Session.query(Event).filter(Event.id == event_id).first()

    @classmethod
    def get_events(cls):
        return Session.query(Event).all()


class Project(BaseObject):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(UnicodeText, default=u'Нет данных')
    promo = Column(String, default="Нет данных")
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    contact_face = Column(String, nullable=False)
    promo_img = Column(String, nullable=True)

    @classmethod
    def get_project_info(cls, project_id):
        return Session.query(Project).filter(Project.id == project_id).first()

    @classmethod
    def get_projects(cls):
        return Session.query(Project).all()


class Order(BaseObject):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Unicode(255), nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    contact_face = Column(Unicode(255))
    event = Column(Integer, ForeignKey('events.id'))
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    address = Column(String, nullable=False)
    count_participants = Column(Integer, default=0)
    note = Column(UnicodeText, default=u'')

    @classmethod
    def get_last_order(cls):
        return Session.query(Order).all()[-1]

    @classmethod
    def get_order_info(cls, order_id):
        return Session.query(Order).filter(Order.id == order_id).first()

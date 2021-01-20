# -*- coding: utf-8 -*-
import os
import sys

import transaction
from pyramid.paster import get_appsettings, setup_logging
from pyramid.scripts.common import parse_vars
from pyramid_sqlalchemy import BaseObject as Base
from pyramid_sqlalchemy import Session as DBSession
from sqlalchemy import engine_from_config, Date, Time
import datetime
from ..models import Event, Project, Order


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def test():
    all_events = Event.get_events()
    all_projects = Project.get_projects()
    order = Order.get_order_info(0)
    print(all_events[0].contact_face)
    print(all_projects[1].name)
    print(order.address)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        event = Event(id=0, name="День первый", description="Nehehe", cost=500,
                      email="my@yandex.ru", phone="+792034", contact_face="Nowhere man")
        event2 = Event(id=1, name="Выпускной", description="NeheheLflflfndnsnfsdkfsdf", cost=500,
                       email="my@yandex.ru", phone="+7920348546578", contact_face="Nowhere man")
        DBSession.add(event)
        DBSession.add(event2)

        everest = Project(id=0, name="EVEREST", description="-", email="laura@laura.com",
                          phone="909090", contact_face="Laura")
        eco = Project(id=1, name="ECOFEST", description="ECOLOGYYYYY", email="yandex@yandex.com",
                      phone="000", contact_face="Tuna")
        health = Project(id=2, name="Health", description="health and food", email="none.com",
                         phone="103", contact_face="Yana")
        DBSession.add(everest)
        DBSession.add(eco)
        DBSession.add(health)

        first_order = Order(id=0, name="EltsynCentre", phone="555", email="eltsyn@gmail.com",
                            contact_face="Boris", event=1, date=datetime.date(year=2021, month=2, day=15),
                            time=datetime.time(hour=19, minute=30), address="Borisa Eltsina 5", count_participants=10)
        second_order = Order(id=1, name="Maria", phone="555", email="Maria@gmail.com",
                             contact_face="Maria", event=1, date=datetime.date(year=2001, month=1, day=2),
                             time=datetime.time(hour=7, minute=59), address="Borisa Eltsina 19", count_participants=10000, note="many meny money")
        DBSession.add(first_order)
        DBSession.add(second_order)
    test()

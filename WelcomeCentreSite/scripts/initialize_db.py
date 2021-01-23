# -*- coding: utf-8 -*-
import os
import sys

import transaction
from pyramid.paster import get_appsettings, setup_logging
from pyramid.scripts.common import parse_vars
from pyramid_sqlalchemy import BaseObject as Base
from pyramid_sqlalchemy import Session as DBSession
from sqlalchemy import engine_from_config
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
    order = Order.get_order_info(1)
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
        first_day = Event(name="День первый",
                          description="День первый в Уральском федеральном — фестиваль для первокурсников "
                                      "и студентов вуза, где каждый найдет что-нибудь себе по душе: "
                                      "нескучные лекции, увлекательные мастер-классы, фудкорт, живую "
                                      "музыку и, конечно же, ярмарку студенческих возможностей. "
                                      "Первокурсникам расскажут о спортивной, творческой, научной, международной "
                                      "и общественной деятельности университета. За выполнение заданий участники "
                                      "ярмарки получат призы с символикой УрФУ.",
                          promo="День первый – общеуниверситетское мероприятие для первокурсников, помогающее "
                                "освоится в Университете и найти занятие по душе.",
                          promo_img="../static/events/first_day.jpg",
                          cost=25000,
                          email="firstdayurfu@yandex.ru",
                          phone="+78005552545",
                          contact_face="Студент УрФУ")
        graduation = Event(name="Выпускной",
                           description="Выпускной УрФУ — второе главное событие в жизни студента. "
                                       "Не передать словами атмосферу всеобщего праздника, "
                                       "когда тысячи студентов на главной университетской площади "
                                       "получают долгожданный диплом под ярким июньским небом "
                                       "в мантии выпускника и конфедератке.\n\n"
                                       "Союз студентов УрФУ принимает участие в организации "
                                       "первых двух этапов и полностью занимается третьим, "
                                       "самым лучшим, не побоимся этого слова, этапом.\n\n"
                                       "На Выпускном уже выступали: Елка, Звери, Пицца, Градусы, "
                                       "Мальбэк&Сюзанна, и это еще не конец списка.",
                           promo="Главный праздник выпускников и всего университета под музыкальное "
                                 "сопровождение любимых артистов и музыкантов.",
                           promo_img="../static/events/graduation.jpg",
                           cost=50000,
                           email="graduation@yandex.ru",
                           phone="+78005552545",
                           contact_face="Асалик Партов")
        eco_lecture = Event(name="Экологический тренинг",
                            description="EcoSpace - новый образовательный проект, где в неформальной обстановке "
                                        "можно послушать о важных и актуальных вещах. Проект проводится при поддержке "
                                        "Эндаумент-фонда УрФУ. Все вырученные средства идут на развитие образования "
                                        "и науки в нашем университете.",
                            promo="EcoSpace — проект Первого направления работы Союза студентов УрФУ, "
                                  "который занимается экологизацией Уральского федерального университета.",
                            promo_img="../static/events/eco_lecture.jpg",
                            cost=5000,
                            email="eco@yandex.ru",
                            phone="+78005552545",
                            contact_face="Грета Тунберг")
        tourism_day = Event(name="День туризма",
                            description="Welcome центр — это студенческий туристический кластер Уральского "
                                        "федерального университета. В структуру центра входят туристические "
                                        "и развлекательные студенческие организации УрФУ, такие как: "
                                        "«День культуры», «EcoSpace», «Твой weekend», «TRIP to TRIP», «САПКИНУ, "
                                        "«Everest», турклубы «Рифей» и «Романтик», а также РЖД бонус.\n\n"
                                        "Проводит крупнейший турестический форум в день туризма.\n\n"
                                        "По вопросам сотрудничества писать на почту.",
                            promo="Туризм есть всё и всё есть туризм.",
                            promo_img="../static/events/tourism_day.jpg",
                            cost=15000,
                            email="tourism@yandex.ru",
                            phone="+78005552545",
                            contact_face="Турист Михайлович")
        brain_storm = Event(name="Хинди",
                            description="Уже совсем скоро, 12 марта, в 18:30 состоится игра «Хинди»💥\n\n"
                                        "«Что это?» — спросите вы. Это старая добрая игра по формату «Катаканы»!\n\n"
                                        "Известная интеллектуальная игра, которая позволит каждому желающему "
                                        "проверить свои знания в кинематографе 📽\n\n"
                                        "Она особо популярна среди киноманов. Также помимо известных фильмов "
                                        "в игре задействованы интересные истории, связанные с популярными актерами, "
                                        "и саундтреки к культовым фильмам.\n\nПодготовка к игре — отличный повод "
                                        "собраться с друзьями и провести вечер, пересматривая любимые фильмы 🍿\n\n"
                                        "На этот раз вопросы игры будут привязаны к прошедшей премии «Оскар».",
                            promo="Интеллектуальная игра от лучшего проекта УрФУ в стиле легендарной Мозгобойни!",
                            promo_img="../static/events/brain_storm.jpg",
                            cost=8000,
                            email="brain@yandex.ru",
                            phone="+78005552545",
                            contact_face="Nowhere man")
        donor_day = Event(name="День донора",
                          description="Забота о своём здоровье — это очень важно, "
                                      "но ещё важнее не забывать помогать нуждающимся!\n\n"
                                      "21 октября у всех желающих будет возможность присоединиться "
                                      "к акции «День донора» от Здоровья в УрФУ\n\nПринять участие "
                                      "могут как первичные доноры, так и вторичные! Кроме того, "
                                      "для вашего удобства будет организован автобус, который отвезёт до "
                                      "пункта сбора крови и обратно!\n\nСбор и отъезд будет осуществляться "
                                      "по адресу ул. Мира, 17! Время сбора участников — 8:10!",
                          promo="Если ты хотел стать донором, но не успел попасть, "
                                "то у тебя появился замечательный шанс!❤",
                          promo_img="../static/events/donor_day.jpg",
                          cost=5000,
                          email="donor@yandex.ru",
                          phone="+79203458753",
                          contact_face="Донор")
        DBSession.add(first_day)
        DBSession.add(graduation)
        DBSession.add(eco_lecture)
        DBSession.add(tourism_day)
        DBSession.add(brain_storm)
        DBSession.add(donor_day)

        everest = Project(name="EVEREST",
                          description="Everest — проект Welcome центра УрФУ, объединяющий не "
                                      "только студентов университета, но и интеллектуальных, интересных, "
                                      "веселых людей, которые любят с пользой проводить время.\n\n"
                                      "Тебя ждет новый формат игр, ставших культовыми. Каждая игра проекта "
                                      "приурочена к какому-либо событию и нацелена на командообразование и "
                                      "повышение уровня знаний в определенных областях жизнедеятельности.",
                          promo="EVEREST - студенческий интеллектуальный проект, проводящий тематические игры!",
                          promo_img="../static/projects/everest.jpg",
                          email="everest@welcome.com",
                          phone="+78005552545",
                          contact_face="Laura")
        eco = Project(name="Эко фест",
                      description="EcoSpace — проект Первого направления работы Союза студентов УрФУ, "
                                  "который занимается экологизацией Уральского федерального университета.\n\n"
                                  "К настоящему моменту проект уже проделал огромную работу по созданию условий "
                                  "для экологичного образа жизни: введен раздельный сбор мусора в ГУКе и установлены "
                                  "контейнеры для сбора батареек в каждом институте.",
                      promo="EcoSpace — проект Первого направления работы Союза студентов УрФУ, "
                            "который занимается экологизацией Уральского федерального университета.",
                      promo_img="../static/projects/eco.jpg",
                      email="eco@welcome.com",
                      phone="+78005552545",
                      contact_face="Tanya")
        health = Project(name="Проект Здоровье",
                         description="Несколько раз в год у студентов есть возможность пройти бесплатное "
                                     "и анонимное тестирование на ВИЧ, а также пройти комплексное обследование. "
                                     "Проект помогает заботиться не только о своем здоровье, но и о "
                                     "здоровье окружающих, в связи с этим дважды в год проводится «День донора». "
                                     "Кроме того, для просвещения студентов в здоровый образ жизни мы организуем "
                                     "«Лекторий здорового человека», где каждый может узнать для себя много нового "
                                     "и полезного, а поддерживать тело в хорошей физической форме помогает "
                                     "еженедельное мероприятие «Спортфест с председателем».",
                         promo="ЗДОРОВЬЕ УрФУ\nВ здоровом теле здоровый дух!",
                         promo_img="../static/projects/health.jpg",
                         email="health@welcome.com",
                         phone="103",
                         contact_face="Yana")
        weekend = Project(name="Твой Weekend",
                          description="Зачем ломать голову о том, как провести свой выходной, "
                                      "если есть Твой WEEKEND — проект Союза студентов, являющийся "
                                      "частью Welcome центр УрФУ.\n\n"
                                      "Благодаря этому проекту ты можешь посетить премьерный "
                                      "показ ожидаемого фильма, сходить в музей, посетить выставку "
                                      "или даже прыгнуть с парашютом.",
                          promo="Позволь спланировать Твой WEEKEND со вкусом, "
                                "обширной программой и неподдельными эмоциями.",
                          promo_img="../static/projects/weekend.jpg",
                          email="weekend@welcome.com",
                          phone="88007558686",
                          contact_face="Maria")
        DBSession.add(everest)
        DBSession.add(eco)
        DBSession.add(health)
        DBSession.add(weekend)

        first_order = Order(name="EltsynCentre", phone="555", email="eltsyn@gmail.com",
                            contact_face="Boris", event=1, date=datetime.date(year=2021, month=2, day=15),
                            time=datetime.time(hour=19, minute=30), address="Бориса Ельцина 5", count_participants=150)
        second_order = Order(name="Maria", phone="555", email="maria@gmail.com",
                             contact_face="Maria", event=2, date=datetime.date(year=2021, month=1, day=2),
                             time=datetime.time(hour=7, minute=59), address="Мира 19",
                             count_participants=10000, note="Хотим яркий выпускной!")
        DBSession.add(first_order)
        DBSession.add(second_order)

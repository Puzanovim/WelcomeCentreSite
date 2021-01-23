# Сайт Welcome Центра

<p>Welcome центр — это студенческий туристический кластер Уральского федерального университета.</p>
<p>В структуру кластера входят множество туристических и развлекательных студенческих организаций УрФУ.</p>

### Описание сайта

<p>Сайт Welcome центра — это информационный портал, в котором собрана актуальная информация о проектах, 
реализуемых Welcome центром УрФУ, и мероприятиях, проводимых данными проектами.</p>
<p>Можно посмотреть описание и стоимость проведения мероприятий. Прочитать о проектах, создающих мероприятия. 
Для каждого проекта и мероприятия указаны телефон и почта, по которым можно связаться с контактным лицом.</p>

<p>Также на сайте расположены все контакты Welcome центра УрФУ в соц.сетях с интерактивной картой.</p>

### Функционал сайта

<p>Сайт Welcome центра позволяет создать заявку на проведение мероприятия. 
После получения заявки менеджер проекта связывается с организацией, 
подавшей заявку для уточнения информации по заказу.</p>

<img src="/WelcomeCentreSite/static/screenshots/Order.jpg" alt="Скриншот заказа">

![alt text](/WelcomeCentreSite/static/screenshots/Order.jpg)

### Инструкция по запуску сайта

Для установки приложения используйте команду:
    
    python setup.py develop 

Установите виртуальное окружение:

    python3 -m venv env

Инициализируйте базу данных с помощью команды:

    initialize_WelcomeCentreSite_db development.ini
    
Теперь можно запускать сервер:

    pserve development.ini
from celery import task
import requests
from coolapp.models import Weather
import smtplib
from email.mime.text import MIMEText
from datetime import timedelta
from celery.task import periodic_task


@periodic_task(run_every=timedelta(seconds=60))
def test():
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?id=520555&units=metric&APPID=cfcce99752884e279099d89454208b16')
    data = response.json()
    w = Weather(city=data['name'], wind=data['wind']['speed'], temp_min=data['main']['temp_min'],
                temp_max=data['main']['temp_max'])
    w.save()


@task
def send_email(email):
    me = 'email@gmail.com'
    you = email
    text = "Добрый день,уважаемый пользователь сайта.Ваш фильм был успешно добавлен"
    subj = "Kinopoisk"
    server = "smtp.gmail.com"
    port = 25
    user_name = "email@gmail.com"
    user_passwd = "passwd"

    msg = MIMEText(text, "", "utf-8")
    msg['Subject'] = subj
    msg['From'] = me
    msg['To'] = you

    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(user_name, user_passwd)
    s.sendmail(me, you, msg.as_string())
    s.quit()

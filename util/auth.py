import datetime

import requests


def auth(year, month, day):
    response = requests.get("https://worldtimeapi.org/api/timezone/Asia/Seoul")
    text = response.json()
    date = text["datetime"].split("T")[0].split("-")
    start = datetime.date(int(date[0]), int(date[1]), int(date[2]))
    end = datetime.date(year, month, day)
    if start > end:
        return False
    else:
        return True


def auth2(year, month, day):
    now = datetime.datetime.now()
    start = datetime.date(now.year, now.month, now.day)
    end = datetime.date(year, month, day)
    if start > end:
        return False
    else:
        return True

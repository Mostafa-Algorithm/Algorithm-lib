# ▄▀█ █░░ █▀▀ █▀█ █▀█ █ ▀█▀ █░█ █▀▄▀█
# █▀█ █▄▄ █▄█ █▄█ █▀▄ █ ░█░ █▀█ █░▀░█

from algorithm.strings import random_string
from fake_email import Email

def get_mail() -> str:
    global mail
    while True:
        mail = Email().Mail()
        if mail['mail'].split("@")[-1] == "omeie.com":
            email = mail['mail']
            return email

def get_pwd(length: int = 16) -> str:
    return random_string(length=length)

def start_listen() -> dict:
    if mail:
        while True:
            inbox = Email(mail['session']).inbox()
            if inbox:
                return {'name': inbox['name'],
                        'from': inbox['from'],
                        'subject': inbox['topic'],
                        'message': inbox['message']}
    else:
        raise Exception('Error in email = %s *_*' %mail)

from threading import Thread
from flask_mail import Message
from app import current_app, mail


def send_async_email(flask_app, msg):
    with flask_app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email(current_app._get_current_object(), msg)).start()

from threading import Thread
from flask import render_template
from flask_mail import Message
from flask_babel import _
from app import app, mail


def send_async_email(flask_app, msg):
    with flask_app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email(app, msg)).start()


def send_password_reset_mail(user):
    token = user.get_reset_password_token()
    send_email(_('[Microblog] Reset your password'), app.config['ADMINS'][0], [user.email],
               render_template('email/reset_password.txt', user=user, token=token),
               render_template('email/reset_password.html', user=user, token=token))

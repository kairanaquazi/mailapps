from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME":'jeffthefreshavocado',
    "MAIL_PASSWORD": 'chickennuggets'
}

app.config.update(mail_settings)
mail = Mail(app)

print("whats yee email?")
email=input()

print("body")
message=input()
if __name__ == '__main__':
    with app.app_context():
        msg = Message(subject="Verify Link",
                      sender='jeffthefreshavocado@gmail.com',
                      recipients=['jeffthefreshavocado@gmail.com',email],
                      body=message)
        mail.send(msg)

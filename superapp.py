from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)


mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": <your email w/o the domain>,
    "MAIL_PASSWORD": <your email password>
}

app.config.update(mail_settings)
mail = Mail(app)

print("what's the email?")
email=input()

print("body")
message=input()

@app.route("/")
def mailsend():
 with app.app_context():
        msg = Message(subject="Verify Link",
                      sender=<your email>,
                      recipients=[email],
                      body=message)
        mail.send(msg)

if __name__ == '__main__':
   app.run(debug=True)

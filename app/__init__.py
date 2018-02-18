from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter some randompassphrase'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = 'e84e76b55c544f' 
app.config['MAIL_PASSWORD'] = 'bfd0999cf269b4'

mail = Mail(app)
from app import views
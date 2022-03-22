from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired

class SignUp(FlaskForm):
    name = StringField("Name")
    login = StringField("Login")
    password = StringField("Password", id='password')
    platform = SelectField(u'Platform', choices=[('coinlist', 'CoinList')])
    registrer = SubmitField("Sign Up")


class SignIn(FlaskForm):
    login = StringField("Login")
    password = StringField("Password", id='password')
    enter = SubmitField("Sign In")
    remember = BooleanField("Remember")

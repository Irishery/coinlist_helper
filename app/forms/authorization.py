from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField

class SignUp(FlaskForm):
    name = StringField("Name", id="name")
    login = StringField("Login", id="login")
    password = StringField("Password", id='password')
    platform = SelectField(u'Platform', id="platform", choices=[('coinlist', 'CoinList')])
    registrer = SubmitField("Sign Up", id="form_button")


class SignIn(FlaskForm):
    login = StringField("Login", id="login")
    password = StringField("Password", id='password')
    enter = SubmitField("Sign In",  id="form_button")
    remember = BooleanField("Remember")

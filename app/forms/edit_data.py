from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField


class EditProfile(FlaskForm):
    platform = SelectField(u'Platform', choices=[('coinlist', 'CoinList')])
    name = StringField("Name",name="name")
    login = StringField("Login", name="login")
    proxy_host = StringField("Proxy Host", name="proxy_host")
    proxy_port = StringField("Proxy Port", name="proxy_port")
    proxy_login = StringField("Proxy Login", name="proxy_login")
    proxy_pass = StringField("Proxy Pass", name="proxy_pass")
    user_agent = StringField("Usre Agent", name="user_agent")
    unmasked_vendor = StringField("Unmasked Vendor", name="unmasked_vendor")
    unmasked_renderer = StringField("Unmasked Renderer", name="unmasked_renderer")
    info = TextAreaField("Info", name="info")
    save = SubmitField("Save")

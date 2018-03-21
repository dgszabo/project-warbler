from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Email, Length


class UserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[Length(min=6)])

class UserEditForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    full_name = StringField('full_name')
    location = StringField('location')
    bio = StringField('bio', widget=TextArea())
    image_url = StringField('image_url')
    header_image_url = StringField('header_image_url')
    password = PasswordField('password', validators=[Length(min=6)])

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[Length(min=6)])

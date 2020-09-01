from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, TextAreaField
from wtforms.validators import DataRequired , Length, Email, EqualTo ,ValidationError
from app.models import User, Developers

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired(), Length(min=5, max=100)])
    confirm_password = StringField('Confirm_Password', validators=[EqualTo('password')])
    submit = SubmitField('SignUp')

    def validation_username(self, username):
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            raise ValidationError('The username already exist username')
    

    def validation_email(self, email):
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            raise ValidationError('The email is already exist')


class DeveloperForm(FlaskForm):
    first_name = StringField('First_Name', validators=[DataRequired()])
    last_name = StringField('Last_Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    address = TextAreaField('Address', validators=[DataRequired()])
    langueges = StringField('Langueges', validators=[DataRequired()])
    level = StringField('Level', validators=[DataRequired()])
    info = TextAreaField('Info', validators=[DataRequired()])
    submit = SubmitField('Add')
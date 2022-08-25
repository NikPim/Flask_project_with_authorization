from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from myproject.models import User

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in!')

class RegistrationForm(FlaskForm):
    email = StringField('Email', [DataRequired(message = "email is necessary"), Email(message="invalid email format")])
    username = StringField('Username', [DataRequired(message = 'email is necessary')])
    password = PasswordField('Password', [DataRequired(),EqualTo('pass_confirm',message = 'Password must match!')])
    pass_confirm = PasswordField('Confirm password', [DataRequired()])
    submit = SubmitField('Register!')
    
    def validate_email(self, email):
        if User.query.filter_by(email = self.email.data).first():
            raise ValidationError('Your email has already been registered!')
            
    def validate_username(self, username):
        if User.query.filter_by(username = self.username.data).first():
            raise ValidationError('This username is taken!')
            
    
            
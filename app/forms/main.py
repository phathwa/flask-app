from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length

class SignUpForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[DataRequired(message="Email is required"), Email(message="Invalid email address")]
    )
    submit = SubmitField('Notify Me')
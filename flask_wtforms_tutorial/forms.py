"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import URL, DataRequired, Email, EqualTo, Length


class ContactForm(FlaskForm):
    """Contact form."""

    name = StringField("Name", [DataRequired()])
    email = StringField(
        "Email",
        [Email(message="Not a valid email address."), DataRequired()]
    )
    body = TextAreaField(
        "Message",
        [DataRequired(), Length(min=4, message="Your message is too short.")]
    )
    submit = SubmitField("Submit")


class SignupForm(FlaskForm):
    """Sign up for a user account."""

    email = StringField(
        "Email",
        [Email(message="Not a valid email address."), DataRequired()]
    )
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirmPassword', message='Passwords must match.')])
    confirmPassword = PasswordField('Confirm password', validators=[DataRequired()])

    title = SelectField(
        "Title",
        [DataRequired()],
        choices=[
            ("Farmer", "farmer"),
            ("Corrupt Politician", "politician"),
            ("No-nonsense City Cop", "cop"),
            ("Professional Rocket League Player", "rocket"),
            ("Lonely Guy At A Diner", "lonely"),
            ("Pokemon Trainer", "pokemon"),
        ],
    )
    website = StringField("Website", validators=[URL()])
    birthday = DateField("Your Birthday")
    submit = SubmitField("Submit")

from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError, HiddenField,FloatField,IntegerField,SubmitField,SelectField,SelectMultipleField,TextAreaField,FileField,Form,DateTimeField,TimeField
from flask_wtf import FlaskForm, Form
from wtforms.fields.html5 import DateField,DateTimeField
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from wtforms_components import TimeField



class ContactForm(Form):
    name = StringField('Name')
    email = StringField('Email', validators=[DataRequired()])
    text = StringField('Text', validators=[DataRequired()])


    submit = SubmitField('Submit')
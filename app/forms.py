from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired

class profileForm(FlaskForm):
    firstname = StringField('firstname', validators=[InputRequired()])
    lastname = StringField('lastname', validators=[InputRequired()])
    age = StringField('age', validators=[InputRequired()])
    gender = SelectField('Gender', choices=[('male','female','other')])
    biography = TextAreaField('biography', validators=[InputRequired()])
    file = FileField('file', validators=[InputRequired()])

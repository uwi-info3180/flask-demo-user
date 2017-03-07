from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

class profileForm(FlaskForm):
    firstname = StringField('firstname', validators=[InputRequired()])
    lastname = StringField('lastname', validators=[InputRequired()])
    age = StringField('age', validators=[InputRequired()])
    biography = StringField('biography', validators=[InputRequired()])

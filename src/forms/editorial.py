from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, URL, Length


class EditorialForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=30)])
    address = StringField('Address', validators=[Length(max=50)])
    city = StringField('City', validators=[Length(max=60)])
    state = StringField('State', validators=[Length(max=30)])
    country = StringField('Country', validators=[Length(max=50)])
    website = StringField('Website', validators=[Length(max=255)])



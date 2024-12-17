from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, SelectField, DateTimeLocalField
from wtforms.validators import DataRequired

CATEGORIES = [('tech', 'Tech'), ('science', 'Science'), ('lifestyle', 'Lifestyle')]

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    category = SelectField('Category', choices=CATEGORIES)
    is_active = BooleanField('Active')
    posted = DateTimeLocalField('Publication Date', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    submit = SubmitField('Submit')

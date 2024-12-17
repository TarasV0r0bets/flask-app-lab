from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, SelectField, DateField
from wtforms.validators import DataRequired

CATEGORIES = [('tech', 'Tech'), ('science', 'Science'), ('lifestyle', 'Lifestyle')]

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    is_active = BooleanField('Active Post')
    publication_date = DateField('Publication Date', format='%Y-%m-%d')
    category = SelectField('Category', choices=CATEGORIES)
    submit = SubmitField('Add Post')

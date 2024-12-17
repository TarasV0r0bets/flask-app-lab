from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
from ..models import User, Tag

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    user_id = SelectField('Author', coerce=int, validators=[DataRequired()])
    tags = SelectMultipleField('Tags', coerce=int)
    is_active = BooleanField('Active')
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.user_id.choices = [(u.id, u.username) for u in User.query.all()]
        self.tags.choices = [(t.id, t.name) for t in Tag.query.all()]

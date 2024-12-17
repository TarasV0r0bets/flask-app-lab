from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class EnterpriseForm(FlaskForm):
    name = StringField('Назва підприємства', validators=[DataRequired()])
    description = TextAreaField('Опис')
    location = StringField('Локація')
    category_id = SelectField('Категорія', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Зберегти')

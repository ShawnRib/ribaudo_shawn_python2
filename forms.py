from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, SelectField
from flask_sqlalchemy import SQLAlchemy


class AddForm(FlaskForm):

    name = StringField('Name of Puppy:')
    color_fur = SelectField(u'Fur color', choices=[('white', 'white'), ('brown', 'brown'), ('black', 'black')])
    submit = SubmitField('Add Puppy')

class AddOwnerForm(FlaskForm):

    name = StringField('Name of Owner:')
    pup_id = IntegerField("Id of Puppy: ")
    submit = SubmitField('Add Owner')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Puppy to Remove:')
    submit = SubmitField('Remove Puppy')

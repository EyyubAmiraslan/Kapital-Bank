from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextField, SubmitField, SelectField
from wtforms.validators import Length, DataRequired, Email, Optional
from wtforms import ValidationError

class CardForm(FlaskForm):
    card_name = StringField('Card Name', [Length(min=2, max=30), DataRequired()])
    card_platform = StringField('Card Platform', [Length(min=2, max=80), DataRequired()])
    card_info = StringField('Card Info', [Length(min=2, max=250), DataRequired()])
    card_price = IntegerField('Card Price', [Optional()])
    card_service = IntegerField('Card Service', [Optional()])
    type_name = SelectField('Card Type', coerce=int )
    card_img = StringField('Card Image', [DataRequired()])
    
    # your_message = TextField('Your Message')





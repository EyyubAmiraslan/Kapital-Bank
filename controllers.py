from flask import render_template, request, redirect
from app import app
from models import Cards, Type
from forms import *

def populate_form_choices(registration_form):
    """
    Pulls choices from the database to populate our select fields.
    """
    types = Type.query.all()
    
    type_choices = list((t.id, t.type_name) for t in types)
    registration_form.type_name.choices = type_choices
    
@app.route("/cards/")
def body():
    cards = Cards.query.all()
    return render_template('body.html', cards=cards)

@app.route('/create_card/', methods=['GET', 'POST'])
def card():
    form = CardForm()
    populate_form_choices(form)
    if request.method == 'POST':
        if form.validate_on_submit():
            card = Cards(card_name=form.card_name.data, card_platform=form.card_platform.data, card_info=form.card_info.data, card_price=form.card_price.data, card_service=form.card_service.data,card_type=form.type_name.data, card_image_url = form.card_img.data)
            card.save()
            return redirect(request.url)
    
    return render_template('ayrica.html', form=form)



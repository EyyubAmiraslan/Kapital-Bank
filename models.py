from extensions  import db


class Cards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(25), nullable=False)
    card_platform = db.Column(db.String(55), nullable=False)
    card_info = db.Column(db.String(150), nullable=False)
    card_price = db.Column(db.Integer)
    card_service = db.Column(db.Integer)
    card_image_url = db.Column(db.String(180), nullable=False)
    card_type= db.Column(db.Integer, db.ForeignKey('type.id'),nullable=False)

    
    
    def __repr__(self):
        return self.card_name
    
    def save(self):
        db.session.add(self)
        db.session.commit()


    # def __init__(self,card_name, card_platform, card_info, card_price, card_service, card_image_url, card_type):
    #     self.card_name = card_name
    #     self.card_platform = card_platform
    #     self.card_info =card_info
    #     self.card_price = card_price
    #     self.card_service = card_service
    #     self.card_image_url = card_image_url
        
    #     self.card_type = card_type

class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(50), nullable=False)
    relations = db.relationship('Cards', backref='cards', lazy=True)


    def __repr__(self):
        return self.type_name
    
    def save(self):
        db.session.add(self)
        db.session.commit()


    def __init__(self, type_name):
        self.type_name = type_name
      





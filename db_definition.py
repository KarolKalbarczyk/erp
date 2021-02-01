from __init__ import db
from enum import Enum

class ProductCategory(Enum):
    Computer = "computer"
    Keyboard = "keyboard"
    Mouse = "mouse"
    Screen = "screen"

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    quantity = db.Column(db.Integer)
    name = db.Column(db.String)
    category = db.Column(db.Enum(ProductCategory))

db.create_all()

#
# db.session.add(Product(code = 'ABCD', quantity = 10, name = 'Asus Rtx101', category = ProductCategory.Computer))
# db.session.add(Product(code = 'ABCD2', quantity = 11, name = 'Titanium V2', category = ProductCategory.Keyboard))
# db.session.add(Product(code = 'ABCD3', quantity = 15, name = 'Titanium V3', category = ProductCategory.Keyboard))
# db.session.add(Product(code = 'ABCD4', quantity = 14, name = 'Logitech G102', category = ProductCategory.Mouse))
# db.session.add(Product(code = 'ABCD5', quantity = 12, name = 'COBRA XS', category = ProductCategory.Mouse))
# db.session.add(Product(code = 'ABCD6', quantity = 16, name = 'Hiro', category = ProductCategory.Computer))
# db.session.commit()
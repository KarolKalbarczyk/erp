from db_definition import Product
from __init__ import db
from product_dto import ProductDTO


class ProductService():

    def get_all_products(self):
        products = Product.query.all()
        dtos = { p.code: {'code': p.code, 'quantity': p.quantity, 'name': p.name, 'category': p.category.value} for p in products }
        return dtos

    def check_requirements(self, requirements):
        products = { p.code: p for p in Product.query.all() }
        answer = {}
        for code, quantity in requirements.items():
            if code in products:
                quantityTaken = min(products[code].quantity, quantity)
                products[code].quantity -= quantityTaken
                answer[code] = quantityTaken

        db.session.commit()
        return answer

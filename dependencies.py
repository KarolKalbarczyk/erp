from injector import singleton

from product_service import ProductService


def configure(binder):

    binder.bind(ProductService, to=ProductService, scope=singleton)

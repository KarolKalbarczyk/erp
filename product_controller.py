import json

from flask import Flask, jsonify, request
from injector import inject

from product_service import ProductService


@inject
def get(service: ProductService):
    dtos = service.get_all_products()
    return jsonify(dtos)

@inject
def order(service: ProductService):
    requirements = request.json['requirements']
    answer = service.check_requirements(requirements)
    return answer

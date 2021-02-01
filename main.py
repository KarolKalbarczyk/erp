from flask_injector import FlaskInjector

import product_controller
from dependencies import configure
from __init__ import app

if __name__ == '__main__':
    app.add_url_rule('/', view_func=product_controller.get)
    app.add_url_rule('/order', view_func=product_controller.order, methods=['POST'])

    FlaskInjector(app=app, modules=[configure])
    app.run(port = 5001)
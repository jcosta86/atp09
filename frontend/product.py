from flask import request, render_template, Blueprint

from backend.controllers.product_controller import read_product, write_product

product = Blueprint(__name__, 'product')


@product.route('/products')
def register_product():
    product_name = request.args.get('produto')
    description = request.args.get('descricao')
    price = request.args.get('preco')

    if (product_name is None) and (description is None) and (price is None):
        pass
    else:
        write_product(product_name, description, price)
    return render_template('products.html', name='olist')


@product.route('/list_products')
def list_products():
    products = read_product()
    return render_template('list_products.html', products=products)

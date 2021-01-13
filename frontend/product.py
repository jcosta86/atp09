from flask import request, render_template, Blueprint, redirect

from backend.controllers.product_controller import read_product, write_product, update_product, delete_product

product = Blueprint(__name__, 'product')


@product.route('/products')
def register_product():
    product_name = request.args.get('product')
    description = request.args.get('description')
    price = request.args.get('price')

    if (product_name is None) and (description is None) and (price is None):
        pass
    else:
        write_product(product_name, description, price)
        return redirect('/list_products')
    return render_template('products.html', name='olist')


@product.route('/list_products')
def list_products():
    products = read_product()
    return render_template('list_products.html', products=products)


@product.route('/products/edit')
def edit_product():
    product_id = request.args.get('id')
    product_name = request.args.get('product')
    description = request.args.get('description')
    product_price = request.args.get('price')
    return render_template('products.html', nome='olist', edit=True, id=product_id, name=product_name, description=description, price=product_price)


@product.route('/products/edit', methods=['POST'])
def save_product_update():
    product_id = request.form.get('id')
    product_name = request.form.get('product')
    description = request.form.get('description')
    product_price = request.form.get('price')
    update_product(product_name, description, product_price, product_id,)
    return redirect('/list_products')


@product.route('/products/delete')
def del_product():
    product_id = request.args.get('id')
    delete_product(product_id)
    return redirect('/list_products')


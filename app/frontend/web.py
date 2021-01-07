import sys
sys.path.append('../app')

from flask import Flask, render_template, request

from backend.global_functions import *
from backend.historic import *

app = Flask(__name__)
name = 'olist'


@app.route('/')
def index():
    return render_template('index.html', name=name, list=menu)


@app.route('/marketplaces')
def register_marketplace():
    marketplace_name = request.args.get('marketplace')
    description = request.args.get('descricao')
    if (marketplace_name is None) and (description is None):
        pass
    else:
        line_in_register = f'"name": "{marketplace_name}", "description": "{description}"'
        save_in_database(line_in_register, 'logs/marketplaces.txt')
        save_log(f'Salvo marketplace - {marketplace_name}')
    return render_template('marketplaces.html', name=name, links=links)


@app.route('/products')
def register_product():
    product_name = request.args.get('produto')
    description = request.args.get('descricao')
    price = request.args.get('preco')
    if (product_name is None) and (description is None) and (price is None):
        pass
    else:
        line_in_register = f'"name": "{product_name}", "description": "{description}", "price": "{price}"'
        save_in_database(line_in_register, 'logs/products.txt')
        save_log(f'Salvo produto - {product_name}')
    return render_template('products.html', name=name, links=links)


@app.route('/categories')
def register_category():
    category_name = request.args.get('category')
    description = request.args.get('descricao')
    if (category_name is None) and (description is None):
        pass
    else:
        line_in_register = f'"name": "{category_name}", "description": "{description}"'
        save_in_database(line_in_register, 'logs/categories.txt')
        save_log(f'Salvo category - {category_name}')
    return render_template('categories.html', name=name, links=links)

@app.route('/sellers')
def register_seller():
    full_name = request.args.get('name')
    email = request.args.get('email')
    phone_number = request.args.get('phone_number')
    if (full_name is None) and (email is None) and (phone_number is None):
        pass
    else:
        line_in_register = f'"name": "{full_name}", "email": "{email}", "phone_number": "{phone_number}"'
        save_in_database(line_in_register, 'logs/sellers.txt')
        save_log(f'Salvo vendedor - {full_name}')
    return render_template('sellers.html', name=name, links=links)


@app.route('/list_marketplaces')
def list_marketplaces():
    marketplaces = read_marketplaces()
    return render_template('list_marketplaces.html', marketplaces=marketplaces)


@app.route('/list_products')
def list_products():
    products = read_products()
    return render_template('list_products.html', products=products)


@app.route('/list_categories')
def list_categories():
    categories = read_categories()
    return render_template('list_categories.html', categories=categories)

@app.route('/list_sellers')
def list_sellers():
    sellers = read_sellers()
    return render_template('list_sellers.html', sellers=sellers)


@app.route('/historico')
def show_historico():
    # lista = lista_historico()
    # return render_template('historico.html', nome=nome, lista=lista, links=links)
    pass

app.run(debug=True)
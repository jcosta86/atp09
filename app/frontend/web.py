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


@app.route('/list-marketplaces')
def list_marketplaces():
    marketplaces = read_marketplaces()
    return render_template('list-marketplaces.html', marketplaces=marketplaces)
    pass

@app.route('/list-products')
def list_products():
    products = read_products()
    return render_template('list-products.html', products=products)


app.run(debug=True)
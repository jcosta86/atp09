import sys
sys.path.append('.')

from flask import Flask, render_template, request
from backend.controllers.category import *
from backend.controllers.marketplace import *
from backend.controllers.product import *
from backend.controllers.seller import *
from backend.utils.utils import read_logfile

app = Flask(__name__)
name = 'olist'

menu = [
    {'name': 'Marketplaces',
     'route': '/marketplaces'},
    {'name': 'Produtos',
     'route': '/products'},
    {'name': 'Categorias',
     'route': '/categories'},
    {'name': 'Vendedores',
     'route': '/sellers'},
     {'name': 'Listar Marketplace',
     'route': '/list_marketplaces'},
    {'name': 'Listar Produtos',
     'route': '/list_products'},
    {'name': 'Listar Categorias',
     'route': '/list_categories'},
    {'name': 'Listar Vendedores',
     'route': '/list_sellers'},
    {'name': 'Log de uso',
     'route': '/logfile'}
]

links = [
    {
        'route': '/',
        'name': 'Voltar'
    },
    {
        'route': 'http://www.olist.com',
        'name': 'olist'
    }
]


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
        write_marketplace(marketplace_name, description)
    return render_template('marketplaces.html', name=name, links=links)


@app.route('/products')
def register_product():
    product_name = request.args.get('produto')
    description = request.args.get('descricao')
    price = request.args.get('preco')

    if (product_name is None) and (description is None) and (price is None):
        pass
    else:
        write_product(product_name, description, price)
    return render_template('products.html', name=name, links=links)


@app.route('/categories')
def register_category():
    category_name = request.args.get('category')
    description = request.args.get('descricao')
    if (category_name is None) and (description is None):
        pass
    else:
        write_category(category_name, description)
    return render_template('categories.html', name=name, links=links)


@app.route('/sellers')
def register_seller():
    full_name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone_number')
    if (full_name is None) and (email is None) and (phone is None):
        pass
    else:
        write_seller(full_name, email, phone)
    return render_template('sellers.html', name=name, links=links)


@app.route('/list_marketplaces')
def list_marketplaces():
    marketplaces = read_marketplace()
    return render_template('list_marketplaces.html', marketplaces=marketplaces)


@app.route('/list_products')
def list_products():
    products = read_product()
    return render_template('list_products.html', products=products)


@app.route('/list_categories')
def list_categories():
    categories = read_categories()
    return render_template('list_categories.html', categories=categories)


@app.route('/list_sellers')
def list_sellers():
    sellers = read_seller()
    return render_template('list_sellers.html', sellers=sellers)


@app.route('/logfile')
def list_historico():
    list_logfile = read_logfile()
    return render_template('logfile.html', lista=list_logfile)
    

app.run(debug=True)
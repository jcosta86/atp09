from flask import Flask, render_template

from frontend.category import category
from frontend.log import log
from frontend.marketplace import marketplace
from frontend.product import product
from frontend.seller import seller

app = Flask(__name__)
app.register_blueprint(marketplace)
app.register_blueprint(product)
app.register_blueprint(category)
app.register_blueprint(seller)
app.register_blueprint(log)

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


@app.route('/')
def index():
    return render_template('index.html', name=name, list=menu)

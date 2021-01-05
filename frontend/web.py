from flask import Flask, render_template, request

from backend.global_functions import *
from backend.markeplace import set_marketplaces
from backend.product import set_product

app = Flask(__name__)
name = 'olist'


@app.route('/')
def index():
    return render_template('index.html', name=name, list=menu)


@app.route('/marketplaces')
def register_marketplace():
    add_mkplace = request.args.get('marketplace')
    description = request.args.get('descricao')
    set_marketplaces(add_mkplace, description)
    return render_template('marketplaces.html', name=name, links=links)


@app.route('/products')
def register_product():
    product = request.args.get('produto')
    description = request.args.get('descricao')
    price = request.args.get('preco')
    set_product(product, description, price)
    return render_template('products.html', name=name, links=links)


@app.route('/historico')
def show_historico():
    # lista = lista_historico()
    # return render_template('historico.html', nome=nome, lista=lista, links=links)
    pass


app.run(debug=True)

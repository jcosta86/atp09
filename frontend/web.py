from flask import Flask, render_template, request

from backend.global_functions import *

app = Flask(__name__)
name = 'olist'


@app.route('/')
def index():
    return render_template('index.html', name=name, list=menu)


@app.route('/marketplaces')
def register_marketplace():
    marketplace_name = request.args.get('marketplace')
    description = request.args.get('descricao')
    line_in_register = f"'name': {marketplace_name}, 'description': {description}"
    save_in_database(line_in_register, 'logs/marketplaces.txt')
    save_log(f'Salvo marketplace - {marketplace_name}')
    return render_template('marketplaces.html', name=name, links=links)


@app.route('/products')
def register_product():
    product_name = request.args.get('produto')
    description = request.args.get('descricao')
    price = request.args.get('preco')
    line_in_register = f"'name: {product_name}, 'description': {description}, 'price': {price}"
    save_in_database(line_in_register, 'logs/products.txt')
    save_log(f'Salvo produto - {product_name}')
    return render_template('products.html', name=name, links=links)


@app.route('/historico')
def show_historico():
    # lista = lista_historico()
    # return render_template('historico.html', nome=nome, lista=lista, links=links)
    pass


app.run(debug=True)
from flask import Flask, render_template, request

from global_functions import *
from markeplace import set_marketplaces
from product import set_product

app = Flask(__name__)
nome = 'olist'


@app.route('/')
def index():
    return render_template('index.html', nome=nome, lista=menu)


@app.route('/marketplaces')
def show_marketplaces():
    return render_template('marketplaces.html', nome=nome)


@app.route('/cadastrarmarketplace')
def cadastro_marketplace():
    add_mkplace = request.args.get('marketplace')
    description = request.args.get('descricao')
    set_marketplaces(add_mkplace, description)
    return render_template('cadastromarketplace.html', links=links)


@app.route('/produtos')
def show_categories():
    return render_template('produtos.html', nome=nome)


@app.route('/cadastroprodutos')
def cadastro_produtos():
    product = request.args.get('produto')
    description = request.args.get('descricao')
    price = request.args.get('preco')
    set_product(product, description, price)
    return render_template('cadastroprodutos.html', links=links)


@app.route('/historico')
def show_historico():
    # lista = lista_historico()
    # return render_template('historico.html', nome=nome, lista=lista, links=links)
    pass


app.run(debug=True)

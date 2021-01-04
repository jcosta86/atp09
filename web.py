from flask import Flask, render_template

from global_functions import *

app = Flask(__name__)
nome = 'olist'


@app.route('/')
def index():
    return render_template('index.html', nome=nome, lista=menu)


@app.route('/marketplaces')
def show_marketplaces():
    pass

@app.route('/produtos')
def show_categories():
    pass

@app.route('/historico')
def show_historico():
    #lista = lista_historico()
    #return render_template('historico.html', nome=nome, lista=lista, links=links)
    pass


app.run(debug=True)

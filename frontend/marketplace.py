from flask import request, render_template, Blueprint

from backend.controllers.marketplace_controller import read_marketplace, write_marketplace

marketplace = Blueprint(__name__, 'marketplace')


@marketplace.route('/marketplaces')
def register_marketplace():
    marketplace_name = request.args.get('marketplace')
    description = request.args.get('descricao')
    if (marketplace_name is None) and (description is None):
        pass
    else:
        write_marketplace(marketplace_name, description)
    return render_template('marketplaces.html', name='olist')


@marketplace.route('/list_marketplaces')
def list_marketplaces():
    marketplaces = read_marketplace()
    return render_template('list_marketplaces.html', marketplaces=marketplaces)

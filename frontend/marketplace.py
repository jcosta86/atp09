from flask import request, render_template, Blueprint, redirect

from backend.controllers.marketplace_controller import MarketplaceController
from backend.models.marketplace_model import Marketplace

marketplace = Blueprint(__name__, 'marketplace')
CONTROLLER = MarketplaceController()


@marketplace.route('/marketplaces')
def register_marketplace():
    marketplace_name = request.args.get('marketplace')
    description = request.args.get('descricao')
    marketplace = Marketplace(marketplace_name, description)
    if (marketplace_name is None) and (description is None):
        pass
    else:
        CONTROLLER.write(marketplace)
        return redirect('/list_marketplaces')
    return render_template('marketplaces.html', name='olist')


@marketplace.route('/list_marketplaces')
def list_marketplaces():
    marketplaces = CONTROLLER.read()
    return render_template('list_marketplaces.html', marketplaces=marketplaces)


@marketplace.route('/marketplaces/update')
def marketplace_update():
    marketplace_id = request.args.get('id')
    marketplace= CONTROLLER.read_by_id(marketplace_id)
    return render_template('marketplaces.html', name='olist', edit=True, marketplace=marketplace)


@marketplace.route('/marketplaces/update', methods=['POST'])
def save_marketplace_update():
    marketplace_id = request.form.get('id')
    marketplace_name = request.form.get('marketplace')
    marketplace_description = request.form.get('descricao')    
    marketplace = CONTROLLER.read_by_id(marketplace_id)
    marketplace.name = marketplace_name
    marketplace.description = marketplace_description
    CONTROLLER.update(marketplace)
    return redirect('/list_marketplaces')


@marketplace.route('/marketplaces/delete')
def marketplace_delete():
    marketplace_id = request.args.get('id')
    marketplace = CONTROLLER.read_by_id(marketplace_id)
    CONTROLLER.delete(marketplace)
    return redirect('/list_marketplaces')


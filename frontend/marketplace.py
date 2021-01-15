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
    id = request.args.get('id')
    marketplace_name = request.args.get('marketplace')
    description = request.args.get('descricao')
    return render_template('marketplaces.html', name='olist', edit=True, id=id, marketplace_name=marketplace_name,
                           description=description)


@marketplace.route('/marketplaces/update', methods=['POST'])
def save_marketplace_update():
    id = request.form.get('id')
    name = request.form.get('marketplace')
    description = request.form.get('descricao')
    marketplace = Marketplace(name, description, id)
    CONTROLLER.update(marketplace)
    return redirect('/list_marketplaces')


@marketplace.route('/marketplaces/delete')
def marketplace_delete():
    id = request.args.get('id')
    CONTROLLER.delete(id)
    return redirect('/list_marketplaces')

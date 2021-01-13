from flask import request, render_template, Blueprint, redirect

from backend.controllers.marketplace_controller import read_marketplace, write_marketplace, update_marketplace, \
    delete_marketplace

marketplace = Blueprint(__name__, 'marketplace')


@marketplace.route('/marketplaces')
def register_marketplace():
    marketplace_name = request.args.get('marketplace')
    description = request.args.get('descricao')
    if (marketplace_name is None) and (description is None):
        pass
    else:
        write_marketplace(marketplace_name, description)
        return redirect('/list_marketplaces')
    return render_template('marketplaces.html', name='olist')


@marketplace.route('/list_marketplaces')
def list_marketplaces():
    marketplaces = read_marketplace()
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
    update_marketplace(id, name, description)
    return redirect('/list_marketplaces')


@marketplace.route('/marketplaces/delete')
def marketplace_delete():
    id = request.args.get('id')
    delete_marketplace(id)
    return redirect('/list_marketplaces')

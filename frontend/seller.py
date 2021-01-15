from flask import request, render_template, Blueprint, redirect

from backend.controllers.seller_controller import SellerController
from backend.models.seller_model import Seller

seller = Blueprint(__name__, 'seller')
CONTROLLER = SellerController()

@seller.route('/sellers')
def register_seller():
    full_name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone_number')
    seller = Seller(full_name, email, phone)
    if (full_name is None) and (email is None) and (phone is None):
        pass
    else:
        CONTROLLER.write(seller)
        return redirect('/list_sellers')
    return render_template('sellers.html', name='olist')


@seller.route('/list_sellers')
def list_sellers():
    sellers = CONTROLLER.read()
    return render_template('list_sellers.html', sellers=sellers)


@seller.route('/sellers/update')
def seller_update():
    seller_id = request.args.get('id')
    seller = CONTROLLER.read_by_id(seller_id)
    return render_template('sellers.html', name='olist', edit=True, seller=seller)


@seller.route('/sellers/update', methods=['POST'])
def save_seller_update():
    id = request.form.get('id')
    full_name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone_number')
    seller = Seller(full_name, email, phone, id)
    CONTROLLER.update(seller)
    return redirect('/list_sellers')


@seller.route('/sellers/delete')
def seller_delete():
    id = request.args.get('id')
    CONTROLLER.delete(id)
    return redirect('/list_sellers')

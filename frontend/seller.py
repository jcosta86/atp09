from flask import request, render_template, Blueprint

from backend.controllers.seller import read_seller, write_seller

seller = Blueprint(__name__, 'seller')


@seller.route('/sellers')
def register_seller():
    full_name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone_number')
    if (full_name is None) and (email is None) and (phone is None):
        pass
    else:
        write_seller(full_name, email, phone)
    return render_template('sellers.html', name='olist')


@seller.route('/list_sellers')
def list_sellers():
    sellers = read_seller()
    return render_template('list_sellers.html', sellers=sellers)

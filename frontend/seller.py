from flask import request, render_template, Blueprint, redirect

from backend.controllers.seller_controller import read_seller, write_seller, update_seller, delete_seller

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
        return redirect('/list_sellers')
    return render_template('sellers.html', name='olist')


@seller.route('/list_sellers')
def list_sellers():
    sellers = read_seller()
    return render_template('list_sellers.html', sellers=sellers)


@seller.route('/sellers/update')
def seller_update():
    id = request.args.get('id')
    full_name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone_number')
    return render_template('sellers.html', name='olist', edit=True, id=id, fullname=full_name, email=email, phone=phone)


@seller.route('/sellers/update', methods=['POST'])
def save_seller_update():
    id = request.form.get('id')
    full_name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone_number')
    update_seller(id, full_name, email, phone)
    return redirect('/list_sellers')


@seller.route('/sellers/delete')
def seller_delete():
    id = request.args.get('id')
    delete_seller(id)
    return redirect('/list_sellers')

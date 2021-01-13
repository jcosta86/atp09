from flask import request, render_template, Blueprint, redirect

from backend.controllers.category_controller import read_categories, write_category, update_category, delete_category

category = Blueprint(__name__, 'category')


@category.route('/categories')
def register_category():
    category_name = request.args.get('category')
    description = request.args.get('descricao')
    if (category_name is None) and (description is None):
        pass
    else:
        write_category(category_name, description)
        return redirect('/list_categories')
    return render_template('categories.html', name='olist', edit=False)


@category.route('/list_categories')
def list_categories():
    categories = read_categories()
    return render_template('list_categories.html', name='olist', categories=categories)


@category.route('/categories/edit')
def edit_category():
    category_id = request.args.get('id')
    category_name = request.args.get('category')
    description = request.args.get('descricao')
    return render_template('categories.html', nome='olist', edit=True, id=category_id, name=category_name, description=description )


@category.route('/categories/edit', methods=['POST'])
def save_category_update():
    category_id = request.form.get('id')
    category_name = request.form.get('category')
    description = request.form.get('descricao')
    update_category(category_name, description, category_id)
    return redirect('/list_categories')

@category.route('/categories/delete')
def del_category():
    category_id = request.args.get('id')
    delete_category(category_id)
    return redirect('/list_categories')

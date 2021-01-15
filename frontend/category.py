from flask import request, render_template, Blueprint, redirect

from backend.controllers.category_controller import CategoryController
from backend.models.category_model import Category

category = Blueprint(__name__, 'category')
CONTROLLER = CategoryController()


@category.route('/categories')
def register_category():
    category_name = request.args.get('category')
    description = request.args.get('description')
    category = Category(category_name, description)
    if (category_name is None) and (description is None):
        pass
    else:
        CONTROLLER.write(category)
        return redirect('/list_categories')
    return render_template('categories.html', name='olist', edit=False)


@category.route('/list_categories')
def list_categories():
    categories = CONTROLLER.read()
    return render_template('list_categories.html', name='olist', categories=categories)


@category.route('/categories/update')
def edit_category():
    category_id = request.args.get('id')
    category = CONTROLLER.read_by_id(category_id)
    return render_template('categories.html', nome='olist', edit=True, category=category )


@category.route('/categories/update', methods=['POST'])
def save_category_update():
    category_id = request.form.get('id')
    category_name = request.form.get('category')
    description = request.form.get('description')
    category = Category(category_name, description, category_id)
    CONTROLLER.update(category)
    return redirect('/list_categories')


@category.route('/categories/delete')
def del_category():
    category_id = request.args.get('id')
    CONTROLLER.delete(category_id)
    return redirect('/list_categories')

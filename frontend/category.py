from flask import request, render_template, Blueprint

from backend.controllers.category import read_categories, write_category
from backend.models.category import Category

category = Blueprint(__name__, 'category')


@category.route('/categories')
def register_category():
    category_name = request.args.get('category')
    description = request.args.get('descricao')
    category = Category(category_name, description)
    if (category_name is None) and (description is None):
        pass
    else:
        write_category(category)
    return render_template('categories.html', name='olist')


@category.route('/list_categories')
def list_categories():
    categories = read_categories()
    return render_template('list_categories.html', categories=categories)

from flask import Blueprint, render_template
from webapp.catalog.models import Price

blueprint = Blueprint('catalog', __name__)


@blueprint.route('/catalog')
def get_products():
    products = Price.query.all() # метод all забираем все товары
    title = "Каталог" # title страницы
    return render_template('catalog/about.html', 
                            page_title=title, 
                            products=products)


#def about():
#    title = "Каталог"
#    return render_template('catalog/about.html', page_title=title)
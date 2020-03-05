from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
index_page = Blueprint('index_page', __name__,
                       template_folder='templates', static_folder='static')



@index_page.route('/index')
@index_page.route('/')
def indox():
    return render_template('index.html')

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
index_page = Blueprint('index_page', __name__,
                       template_folder='templates', static_folder='static')



@index_page.route('/index')
@index_page.route('/')
def index():
    body_string = "Welcome, we are a small team of developers. Our games are passion projects. While our games are a way from public viewing, we hope you'll like our many offerings. We're currently building this place, so please don't' mind the dust."
    return render_template('index.html', title="Index", body=body_string.replace('\n', '<br>'))


@index_page.route('/about')
def about():
    body_string = "Jim Marsden - Programming\nInsula - Art, Game Design\nDivi - Game Design, Quality Assurance"
    return render_template('index.html', title="About", body=body_string.replace('\n', '<br>'))



@index_page.route('/try_it')
def try_it():
    body_string = "Sorry, we don't have anything just yet. :c"
    return render_template('index.html', title="try it", body=body_string.replace('\n', '<br>'))
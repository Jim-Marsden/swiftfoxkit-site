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
    github_link = '<a href="https://github.com/Jim-Marsden/Purrmaid"> Purrmaid </a>'


    project = f"""We use our own game engine {github_link}
    While we don't have much in the way of details on our first project public at the moment, it will be a retail focused game."""
    team = "The team: Jim Marsden - Programming\nInsula - Art, Game Design\nDivi - Game Design, Quality Assurance"


    return render_template('about.html', title="About", team_header="Our team:", project_header="Our projects:",
                           project_body=project.replace('\n', '<br>'), team_body=team.replace('\n', '<br>'))



@index_page.route('/try_it')
def try_it():
    body_string = "Sorry, we don't have anything just yet. :c"
    return render_template('index.html', title="try it", body=body_string.replace('\n', '<br>'))


@index_page.route('/thanks')
def thanks():
    body_string = """We would like to thank the following people:
    <br>
            From Jim:
    <ul>"""

    people_to_thank_jim = {"Keeva" : "Putting up with me",
                       "Insula": "All of the art, and helping me focus",
                       "Nyletak": "Getting the art started", }

    people_to_thank_insula = {
        "Valsharen": "being a supportive spouse",
        "Browncoat": "giving the best worst ideas"
    }

    for x, y in people_to_thank_jim.items():
        body_string += "\n\t\t"
        body_string += F"<li> {x} for {y.lower()}</li>"

    body_string += "</ul> \n        From Insula: <ul>"

    for x, y in people_to_thank_insula.items():
        body_string += "\n"
        body_string += F"<li> {x} for {y.lower()}</li>"


    return render_template('index.html', title="Thanks", body=body_string)




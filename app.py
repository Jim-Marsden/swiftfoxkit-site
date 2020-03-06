from flask import Flask

import  index

app = Flask(__name__)
app.register_blueprint(index.index_page)


if __name__ == '__main__':
    app.run(debug=True)

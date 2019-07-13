from flask import Flask, render_template
from codes.route.login import login_bp, loginManager
from codes.route.search import search_bp
from codes.route.register import register_bp
from codes.route.index import index_bp
from codes.persist.database import db,DB_URI

import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    key = os.urandom(24)
    app.config['SECRET_KEY'] = key
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    loginManager.setup_app(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    db.init_app(app)
    app.register_blueprint(login_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(index_bp)
    app.run()

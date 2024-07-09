import os
from flask import Flask
from .extensions import Bootstrap5, db, migrate
from .routes import main

FLASK_SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = FLASK_SECRET_KEY
    Bootstrap5(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app

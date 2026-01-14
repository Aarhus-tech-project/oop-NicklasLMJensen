from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db




def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'

    db.init_app(app)

    from pages import bp
    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()

    return app
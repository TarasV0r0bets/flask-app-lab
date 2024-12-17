from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    db.init_app(app)
    migrate.init_app(app, db)

    # Реєстрація Blueprint
    from .posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix="/posts")

    return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()  # Оголошуємо SQLAlchemy
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Ініціалізуємо розширення
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Реєструємо Blueprint
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app

from flask import Flask
from app.users.views import users_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(users_bp, url_prefix='/users')

    @app.route('/')
    def index():
        return "Welcome to the Flask App! Go to /users/hi/<name> to see a greeting."

    return app

app = create_app()

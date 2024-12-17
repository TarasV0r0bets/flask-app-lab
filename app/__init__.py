from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    
    from .posts import post_bp
    app.register_blueprint(post_bp, url_prefix="/posts")
    
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404
    
    return app

from flask import Blueprint, render_template, request

users_bp = Blueprint('users', __name__, template_folder='templates')

@users_bp.route('/hi/<name>')
def greetings(name):
    age = request.args.get('age', 'N/A')
    return render_template('users/hi.html', name=name.upper(), age=age)

@users_bp.route('/admin')
def admin():
    return "ADMINISTRATOR, age: 45"

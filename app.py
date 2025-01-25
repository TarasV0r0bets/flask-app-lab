import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from forms import RegistrationForm, LoginForm
from models import db, bcrypt, User

# Ініціалізація Flask-додатку
app = Flask(__name__)

# Конфігурація додатку
basedir = os.path.abspath(os.path.dirname(__file__))  # Базова директорія проекту
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'database', 'users.db')}"  # Шлях до бази даних
app.config['SECRET_KEY'] = 'your_secret_key'  # Секретний ключ для сесій
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Вимкнення попередження

# Ініціалізація розширень
db.init_app(app)  # Зв'язок SQLAlchemy з додатком Flask
bcrypt.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Завантаження користувача для Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Головна сторінка
@app.route('/')
def home():
    return 'Welcome to the Flask App! Go to /register or /login to get started.'

# Сторінка реєстрації
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash('Email is already registered!', 'danger')
            return redirect(url_for('register'))
        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# Сторінка входу
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('account'))
        flash('Invalid credentials', 'danger')
    return render_template('login.html', form=form)

# Сторінка профілю
@app.route('/account')
@login_required
def account():
    return render_template('account.html', user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# Створення таблиць перед запуском
if __name__ == '__main__':
    # Переконайтесь, що папка для бази даних існує
    db_dir = os.path.join(basedir, 'database')
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
    
    # Ініціалізація бази даних
    with app.app_context():
        db.create_all()
    
    # Запуск додатка
    app.run(debug=True)

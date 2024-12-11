from flask import Flask, render_template, request, redirect, url_for, flash, session, make_response

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Дані для автентифікації
users = {
    'user1': 'password123',
    'user2': 'password456'
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            flash(f'Привіт, {username}!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Невірне ім\'я користувача або пароль', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        flash('Будь ласка, увійдіть у систему', 'danger')
        return redirect(url_for('login'))

    username = session['username']

    if request.method == 'POST':
        if 'add_cookie' in request.form:
            key = request.form['cookie_key']
            value = request.form['cookie_value']
            expires = request.form['expires']
            resp = make_response(redirect(url_for('profile')))
            resp.set_cookie(key, value, max_age=int(expires))
            flash(f'Кукі {key} додано з терміном дії {expires} секунд', 'success')
            return resp
        
        elif 'delete_cookie' in request.form:
            key = request.form['delete_key']
            resp = make_response(redirect(url_for('profile')))
            resp.delete_cookie(key)
            flash(f'Кукі {key} видалено', 'success')
            return resp

    cookies = request.cookies.items()

    return render_template('profile.html', username=username, cookies=cookies)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Ви вийшли з системи', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

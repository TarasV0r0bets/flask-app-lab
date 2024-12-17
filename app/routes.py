from flask import render_template, url_for, flash, redirect, request
from flask_login import login_required, current_user
from app import app, db
from app.forms import UpdateAccountForm, LoginForm
from app.models import User
from datetime import datetime


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.about_me = form.about_me.data
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
        flash('Ваш профіль успішно оновлено!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.about_me.data = current_user.about_me
    return render_template('account.html', title='Account', form=form)

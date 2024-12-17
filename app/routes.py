from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import db, Enterprise, Category
from app.forms import EnterpriseForm

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    enterprises = Enterprise.query.order_by(Enterprise.name).all()
    return render_template('index.html', enterprises=enterprises)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = EnterpriseForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.all()]
    if form.validate_on_submit():
        enterprise = Enterprise(
            name=form.name.data,
            description=form.description.data,
            location=form.location.data,
            category_id=form.category_id.data,
            created_by=current_user.id
        )
        db.session.add(enterprise)
        db.session.commit()
        flash('Підприємство успішно додано!', 'success')
        return redirect(url_for('main.index'))
    return render_template('create.html', form=form)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    enterprise = Enterprise.query.get_or_404(id)
    if enterprise.created_by != current_user.id:
        flash('Ви не маєте прав для редагування цього запису.', 'danger')
        return redirect(url_for('main.index'))
    form = EnterpriseForm(obj=enterprise)
    form.category_id.choices = [(c.id, c.name) for c in Category.query.all()]
    if form.validate_on_submit():
        enterprise.name = form.name.data
        enterprise.description = form.description.data
        enterprise.location = form.location.data
        enterprise.category_id = form.category_id.data
        db.session.commit()
        flash('Запис оновлено!', 'success')
        return redirect(url_for('main.index'))
    return render_template('edit.html', form=form)

@bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    enterprise = Enterprise.query.get_or_404(id)
    if enterprise.created_by != current_user.id:
        flash('Ви не маєте прав для видалення цього запису.', 'danger')
        return redirect(url_for('main.index'))
    db.session.delete(enterprise)
    db.session.commit()
    flash('Запис видалено!', 'success')
    return redirect(url_for('main.index'))

@bp.route('/detail/<int:id>')
def detail(id):
    enterprise = Enterprise.query.get_or_404(id)
    return render_template('detail.html', enterprise=enterprise)

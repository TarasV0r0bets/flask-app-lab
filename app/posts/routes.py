from flask import render_template, redirect, url_for, flash, request
from . import bp
from .forms import PostForm
from ..models import Post
from .. import db

@bp.route('/')
def all_posts():
    posts = Post.query.order_by(Post.posted.desc()).all()
    return render_template('all_posts.html', posts=posts)

@bp.route('/add', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            category=form.category.data,
            is_active=form.is_active.data,
            posted=form.posted.data,
            author="Admin"
        )
        db.session.add(post)
        db.session.commit()
        flash('Post added successfully!', 'success')
        return redirect(url_for('posts.all_posts'))
    return render_template('add_post.html', form=form)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    post = Post.query.get_or_404(id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.category = form.category.data
        post.is_active = form.is_active.data
        post.posted = form.posted.data
        db.session.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('posts.all_posts'))
    return render_template('edit_post.html', form=form, post=post)

@bp.route('/delete/<int:id>')
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('posts.all_posts'))

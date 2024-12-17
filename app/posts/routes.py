from flask import render_template, redirect, url_for, flash
from . import bp
from .forms import PostForm
from ..models import Post, User, Tag
from .. import db

@bp.route('/')
def all_posts():
    posts = Post.query.all()
    return render_template('all_posts.html', posts=posts)

@bp.route('/add', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            is_active=form.is_active.data,
            user_id=form.user_id.data
        )
        selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data)).all()
        post.tags.extend(selected_tags)
        db.session.add(post)
        db.session.commit()
        flash('Post added successfully!', 'success')
        return redirect(url_for('posts.all_posts'))
    return render_template('add_post.html', form=form)

@bp.route('/')
def all_posts():
    posts = Post.query.all()
    return render_template('all_posts.html', posts=posts)

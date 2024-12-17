from flask import render_template, redirect, url_for, flash
from . import post_bp
from .forms import PostForm
import json, os

POSTS_FILE = "posts.json"

def load_posts():
    if os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_posts(posts):
    with open(POSTS_FILE, 'w') as file:
        json.dump(posts, file, indent=4)

@post_bp.route('/add', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    posts = load_posts()
    if form.validate_on_submit():
        post = {
            "id": len(posts) + 1,
            "title": form.title.data,
            "content": form.content.data,
            "category": form.category.data,
            "is_active": form.is_active.data,
            "publication_date": str(form.publication_date.data),
            "author": "SessionUser"
        }
        posts.append(post)
        save_posts(posts)
        flash(f"Post '{form.title.data}' added successfully!", 'success')
        return redirect(url_for('posts.add_post'))
    return render_template('add_post.html', form=form)

#!/usr/bin/env python
# encoding: utf-8
from main import app, db
from models import BlogPosts


from flask import render_template, request, redirect


@app.route('/', methods=['GET', 'POST'])
def info():
    blogposts = BlogPosts.query.all()
    return render_template('info.html', blogposts=blogposts)

@app.route('/new-post', methods=['POST'])
def new_post():
    content = request.form['content']
    post = BlogPosts(text=content, subject="Nowy post")
    db.session.add(post)
    db.session.commit()
    return redirect('/')
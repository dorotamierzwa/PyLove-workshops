#!/usr/bin/env python
# encoding: utf-8
from main import app, db
from models import BlogPosts, User


from flask import render_template, request, redirect
import random
from datetime import datetime


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


@app.route('/edit/<ide>', methods=['POST', 'GET'])
def edit_post(ide):
    if request.method == 'POST':
        post = BlogPosts.query.filter_by(id=ide).first()
        edited_content = request.form['edited_content']
        edited_subject = request.form['edited_subject']
        post.text = edited_content
        post.subject = edited_subject
        db.session.commit()
        return redirect('/')

    return render_template('edit_post.html', ide=ide)

@app.route('/delete/<ide>', methods=['POST'])
def delete_post(ide):
    post = BlogPosts.query.filter_by(id=ide).first()
    db.session.delete(post)
    db.session.commit()
    return redirect('/')

@app.route('/about-me', methods=['GET'])
def about():
    user = User(id=1, email='dorota@gmail.com')
    db.session.add(user)
    return render_template('about-me.html', user=user)

@app.route('/search-results', methods=['POST', 'GET'])
def search_posts():
    blogposts = BlogPosts.query.all()
    if request.method == 'POST':
        search_subject = request.form['search_subject']
        search_content = request.form['search_content']
        return render_template('search-results.html', search_content=search_content, search_subject=search_subject,
                               blogposts=blogposts)

@app.route('/lucky', methods=['GET'])
def feelin_lucky():
    blogposts = BlogPosts.query.all()
    lucky_post = random.choice(blogposts)
    return render_template('lucky.html', lucky_post=lucky_post)

from flask import render_template, request, redirect, jsonify
from main import app
from models import Product, Review


@app.route('/', methods=['GET', 'POST'])
def show_product():
    products = Product.query.all()
    reviews = Review.query.all()
    return render_template('product_list.html', products=products, reviews=reviews)

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify({products})\

@app.route('/products/<int:p_id>', methods=['GET'])
def get_each_product():
    products = Product.query.all()
    for product in products:
        if product.id == p_id:
            return jsonify({product})

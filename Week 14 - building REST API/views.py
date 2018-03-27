from flask import render_template, request, redirect
import random
from main import app
from models import Product


@app.route('/', methods=['GET', 'POST'])
def show_product():
    products = Product.query.all()
    return render_template('product_list.html', products=products)
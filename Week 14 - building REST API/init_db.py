from sqlalchemy import create_engine

from main import db
import models


def db_start():
    create_engine('sqlite:///tmp/testapi.db', convert_unicode=True)
    db.create_all()
    db.session.commit()
    product_1 = models.Product()
    product_1.name = 'Computer'
    product_1.description = 'Very big comupter'
    product_1.category = 'Personal computer'
    db.session.add(product_1)
    db.session.commit()

    review_1 = models.Review()
    review_1.author = 'Johny'
    review_1.text = 'Very nice computer'
    review_1.rating = 5
    review_1.product_id = 1
    db.session.add(review_1)
    db.session.commit()

if __name__ == '__main__':
    db_start()
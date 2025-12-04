# endpoints/products.py
from flask_restful import Resource, reqparse
from flask import request
from auth_decorator import require_auth
from repositories.product_repository import ProductRepository

class ProductsResource(Resource):
    def __init__(self):
        self.repository = ProductRepository('db.json')
        self.parser = reqparse.RequestParser()
        self.setup_parser()
    
    def setup_parser(self):
        self.parser.add_argument('name', type=str, required=True, 
                               help='Name of the product')
        self.parser.add_argument('category', type=str, required=True,
                               help='Category of the product')
        self.parser.add_argument('price', type=float, required=True,
                               help='Price of the product')
    
    @require_auth
    def get(self, product_id=None):
        category_filter = request.args.get('category')
        
        if category_filter:
            products = self.repository.filter_by_category(category_filter)
            return products
        
        if product_id is not None:
            product = self.repository.get_by_id(product_id)
            if product:
                return product
            return {'message': 'Product not found'}, 404
        
        return self.repository.get_all()
    
    @require_auth
    def post(self):
        args = self.parser.parse_args()
        new_product = {
            'name': args['name'],
            'category': args['category'],
            'price': args['price']
        }
        
        product = self.repository.add(new_product)
        return {'message': 'Product added', 'product': product}, 201
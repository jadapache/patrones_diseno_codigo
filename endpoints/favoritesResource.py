# endpoints/favorites.py
from flask_restful import Resource, reqparse
from auth_decorator import require_auth
from repositories.favorite_repository import FavoriteRepository

class FavoritesResource(Resource):
    def __init__(self):
        self.repository = FavoriteRepository('favorites.json')
        self.parser = reqparse.RequestParser()
        self.setup_parser()
    
    def setup_parser(self):
        self.parser.add_argument('user_id', type=int, required=True,
                               help='User ID')
        self.parser.add_argument('product_id', type=int, required=True,
                               help='Product ID')
    
    @require_auth
    def get(self):
        return self.repository.get_all(), 200
    
    @require_auth
    def post(self):
        args = self.parser.parse_args()
        new_favorite = {
            'user_id': args['user_id'],
            'product_id': args['product_id']
        }
        favorite = self.repository.add(new_favorite)
        return {'message': 'Product added to favorites', 'favorite': favorite}, 201
    
    @require_auth
    def delete(self):
        args = self.parser.parse_args()
        self.repository.delete(args['user_id'], args['product_id'])
        return {'message': 'Product removed from favorites'}, 200
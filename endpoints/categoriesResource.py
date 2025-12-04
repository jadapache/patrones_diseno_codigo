# endpoints/categories.py
from flask_restful import Resource, reqparse
from auth_decorator import require_auth
from repositories.category_repository import CategoryRepository

class CategoriesResource(Resource):
    def __init__(self):
        self.repository = CategoryRepository('db.json')
        self.parser = reqparse.RequestParser()
        self.setup_parser()
    
    def setup_parser(self):
        self.parser.add_argument('name', type=str, required=True,
                               help='Name of the category')
    
    @require_auth
    def get(self, category_id=None):
        if category_id is not None:
            category = self.repository.get_by_id(category_id)
            if category:
                return category
            return {'message': 'Category not found'}, 404
        
        return self.repository.get_all()
    
    @require_auth
    def post(self):
        args = self.parser.parse_args()
        category_name = args['name']
        
        if not category_name:
            return {'message': 'Category name is required'}, 400
        
        existing = self.repository.get_by_name(category_name)
        if existing:
            return {'message': 'Category already exists'}, 400
        
        new_category = {'name': category_name}
        category = self.repository.add(new_category)
        return {'message': 'Category added successfully', 'category': category}, 201
    
    @require_auth
    def delete(self):
        args = self.parser.parse_args()
        category_name = args['name']
        
        if not category_name:
            return {'message': 'Category name is required'}, 400
        
        existing = self.repository.get_by_name(category_name)
        if not existing:
            return {'message': 'Category not found'}, 404
        
        self.repository.delete_by_name(category_name)
        return {'message': 'Category removed successfully'}, 200
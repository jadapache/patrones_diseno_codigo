# app.py
from flask import Flask
from flask_restful import Api
from endpoints.products import ProductsResource
from endpoints.auth import AuthenticationResource
from endpoints.categories import CategoriesResource
from endpoints.favorites import FavoritesResource

def create_app():
    app = Flask(__name__)
    api = Api(app)
    
    # Configuración de rutas
    api.add_resource(AuthenticationResource, '/auth')
    api.add_resource(ProductsResource, '/products', '/products/<int:product_id>')
    api.add_resource(CategoriesResource, '/categories', '/categories/<int:category_id>')
    api.add_resource(FavoritesResource, '/favorites')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
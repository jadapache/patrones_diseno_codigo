from repository.base_repository import BaseRepository

class ProductRepository(BaseRepository):
    def get_all(self):
        return self.data.get('products', [])

    def get_by_id(self, product_id):
        products = self.get_all()
        return next((p for p in products if p['id'] == product_id), None)

    def add(self, product):
        products = self.get_all()
        product['id'] = len(products) + 1
        products.append(product)
        self.data['products'] = products
        self.save_data()
        return product

    def filter_by_category(self, category):
        products = self.get_all()
        return [p for p in products if p['category'].lower() == category.lower()]


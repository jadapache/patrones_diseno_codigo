from repository.base_repository import BaseRepository


class CategoryRepository(BaseRepository):
    def get_all(self):
        return self.data.get('categories', [])

    def get_by_id(self, category_id):
        categories = self.get_all()
        return next((c for c in categories if c['id'] == category_id), None)

    def get_by_name(self, name):
        categories = self.get_all()
        return next((c for c in categories if c['name'] == name), None)

    def add(self, category):
        categories = self.get_all()
        category['id'] = len(categories) + 1
        categories.append(category)
        self.data['categories'] = categories
        self.save_data()
        return category

    def delete_by_name(self, name):
        categories = self.get_all()
        categories = [c for c in categories if c['name'] != name]
        self.data['categories'] = categories
        self.save_data()


from repository.base_repository import BaseRepository


class FavoriteRepository(BaseRepository):
    def get_all(self):
        return self.data.get('favorites', [])

    def add(self, favorite):
        favorites = self.get_all()
        favorites.append(favorite)
        self.data['favorites'] = favorites
        self.save_data()
        return favorite

    def delete(self, user_id, product_id):
        favorites = self.get_all()
        favorites = [f for f in favorites
                     if not (f['user_id'] == user_id and f['product_id'] == product_id)]
        self.data['favorites'] = favorites
        self.save_data()

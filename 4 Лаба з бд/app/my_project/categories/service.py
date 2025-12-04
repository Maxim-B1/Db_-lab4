from .dao import CategoriesDAO
from .domain import Category

class CategoriesService:
    def __init__(self):
        self.dao = CategoriesDAO()

    def get_all(self):
        rows = self.dao.get_all()
        return [Category.from_dict(r).to_dict() for r in rows]

    def get_by_id(self, category_id):
        r = self.dao.get_by_id(category_id)
        return Category.from_dict(r).to_dict() if r else None

    def create(self, data):
        name = data.get("name")
        description = data.get("description")
        new_id = self.dao.create(name, description)
        return new_id

    def update(self, category_id, data):
        name = data.get("name")
        description = data.get("description")
        return self.dao.update(category_id, name, description)

    def delete(self, category_id):
        return self.dao.delete(category_id)

    def get_categories_with_drugs(self):
        return self.dao.get_categories_with_drugs()


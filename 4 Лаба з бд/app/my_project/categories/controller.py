from .service import CategoriesService

class CategoriesController:
    def __init__(self):
        self.svc = CategoriesService()

    def get_all(self):
        return self.svc.get_all()

    def get_by_id(self, category_id):
        return self.svc.get_by_id(category_id)

    def create(self, data):
        return self.svc.create(data)

    def update(self, category_id, data):
        return self.svc.update(category_id, data)

    def delete(self, category_id):
        return self.svc.delete(category_id)

    def get_categories_with_drugs(self):
        return self.svc.get_categories_with_drugs()


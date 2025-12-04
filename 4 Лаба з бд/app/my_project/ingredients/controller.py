from .service import IngredientsService

class IngredientsController:
    def __init__(self):
        self.svc = IngredientsService()

    def get_all(self):
        return self.svc.get_all()

    def get_by_id(self, iid):
        return self.svc.get_by_id(iid)

    def create(self, data):
        return self.svc.create(data)

    def update(self, iid, data):
        return self.svc.update(iid, data)

    def delete(self, iid):
        return self.svc.delete(iid)

    def get_with_ingredients(self):
        return self.svc.get_with_ingredients()

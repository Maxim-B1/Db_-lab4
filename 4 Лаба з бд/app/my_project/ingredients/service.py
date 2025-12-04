from .dao import IngredientsDAO
from .domain import Ingredient

class IngredientsService:
    def __init__(self):
        self.dao = IngredientsDAO()

    def get_all(self):
        rows = self.dao.get_all()
        return [Ingredient.from_dict(r).to_dict() for r in rows]

    def get_by_id(self, iid):
        r = self.dao.get_by_id(iid)
        return Ingredient.from_dict(r).to_dict() if r else None

    def create(self, data):
        return self.dao.create(data.get("name"), data.get("description"))

    def update(self, iid, data):
        return self.dao.update(iid, data.get("name"), data.get("description"))

    def delete(self, iid):
        return self.dao.delete(iid)

    def get_with_ingredients(self):
        return self.dao.get_with_ingredients()

from .dao import ManufacturersDAO
from .domain import Manufacturer

class ManufacturersService:
    def __init__(self):
        self.dao = ManufacturersDAO()

    def get_all(self):
        rows = self.dao.get_all()
        return [Manufacturer.from_dict(r).to_dict() for r in rows]

    def get_by_id(self, mid):
        r = self.dao.get_by_id(mid)
        return Manufacturer.from_dict(r).to_dict() if r else None

    def create(self, data):
        return self.dao.create(data.get("name"), data.get("country"), data.get("contact_info"))

    def update(self, mid, data):
        return self.dao.update(mid, data.get("name"), data.get("country"), data.get("contact_info"))

    def delete(self, mid):
        return self.dao.delete(mid)

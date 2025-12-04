from .dao import SuppliersDAO
from .domain import Supplier

class SuppliersService:
    def __init__(self):
        self.dao = SuppliersDAO()

    def get_all(self):
        rows = self.dao.get_all()
        return [Supplier.from_dict(r).to_dict() for r in rows]

    def get_by_id(self, sid):
        r = self.dao.get_by_id(sid)
        return Supplier.from_dict(r).to_dict() if r else None

    def create(self, data):
        return self.dao.create(data.get("name"), data.get("country"), data.get("contact_info"))

    def update(self, sid, data):
        return self.dao.update(sid, data.get("name"), data.get("country"), data.get("contact_info"))

    def delete(self, sid):
        return self.dao.delete(sid)

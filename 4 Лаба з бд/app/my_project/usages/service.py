from .dao import UsagesDAO
from .domain import Usage

class UsagesService:
    def __init__(self):
        self.dao = UsagesDAO()

    def get_all(self):
        rows = self.dao.get_all()
        return [Usage.from_dict(r).to_dict() for r in rows]

    def get_by_id(self, uid):
        r = self.dao.get_by_id(uid)
        return Usage.from_dict(r).to_dict() if r else None

    def create(self, data):
        return self.dao.create(data.get("description"))

    def update(self, uid, data):
        return self.dao.update(uid, data.get("description"))

    def delete(self, uid):
        return self.dao.delete(uid)

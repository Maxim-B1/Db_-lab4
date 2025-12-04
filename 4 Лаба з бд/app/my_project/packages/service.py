from .dao import PackagesDAO
from .domain import Package

class PackagesService:
    def __init__(self):
        self.dao = PackagesDAO()

    def get_all(self):
        rows = self.dao.get_all()
        return [Package.from_dict(r).to_dict() for r in rows]

    def get_by_id(self, pid):
        r = self.dao.get_by_id(pid)
        return Package.from_dict(r).to_dict() if r else None

    def create(self, data):
        return self.dao.create(data.get("type"), data.get("quantity"))

    def update(self, pid, data):
        return self.dao.update(pid, data.get("type"), data.get("quantity"))

    def delete(self, pid):
        return self.dao.delete(pid)

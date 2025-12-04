from .service import ManufacturersService

class ManufacturersController:
    def __init__(self):
        self.svc = ManufacturersService()

    def get_all(self):
        return self.svc.get_all()

    def get_by_id(self, mid):
        return self.svc.get_by_id(mid)

    def create(self, data):
        return self.svc.create(data)

    def update(self, mid, data):
        return self.svc.update(mid, data)

    def delete(self, mid):
        return self.svc.delete(mid)

from .service import SuppliersService

class SuppliersController:
    def __init__(self):
        self.svc = SuppliersService()

    def get_all(self):
        return self.svc.get_all()

    def get_by_id(self, sid):
        return self.svc.get_by_id(sid)

    def create(self, data):
        return self.svc.create(data)

    def update(self, sid, data):
        return self.svc.update(sid, data)

    def delete(self, sid):
        return self.svc.delete(sid)

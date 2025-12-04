from .service import UsagesService

class UsagesController:
    def __init__(self):
        self.svc = UsagesService()

    def get_all(self):
        return self.svc.get_all()

    def get_by_id(self, uid):
        return self.svc.get_by_id(uid)

    def create(self, data):
        return self.svc.create(data)

    def update(self, uid, data):
        return self.svc.update(uid, data)

    def delete(self, uid):
        return self.svc.delete(uid)

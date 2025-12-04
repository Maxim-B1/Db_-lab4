from .service import PackagesService

class PackagesController:
    def __init__(self):
        self.svc = PackagesService()

    def get_all(self):
        return self.svc.get_all()

    def get_by_id(self, pid):
        return self.svc.get_by_id(pid)

    def create(self, data):
        return self.svc.create(data)

    def update(self, pid, data):
        return self.svc.update(pid, data)

    def delete(self, pid):
        return self.svc.delete(pid)

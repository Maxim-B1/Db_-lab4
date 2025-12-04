from .service import DrugsService

class DrugsController:
    def __init__(self):
        self.svc = DrugsService()

    def get_all(self):
        return self.svc.get_all()

    def get_by_id(self, drug_id):
        return self.svc.get_by_id(drug_id)

    def create(self, data):
        return self.svc.create(data)

    def update(self, drug_id, data):
        return self.svc.update(drug_id, data)

    def delete(self, drug_id):
        return self.svc.delete(drug_id)

    def get_drugs_by_manufacturers(self):
        return self.svc.get_drugs_by_manufacturers()

    def get_drugs_with_ingredients(self):
        return self.svc.get_drugs_with_ingredients()

    def get_drugs_with_usages(self):
        return self.svc.get_drugs_with_usages()

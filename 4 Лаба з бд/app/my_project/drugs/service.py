from .dao import DrugsDAO

class DrugsService:
    def __init__(self):
        self.dao = DrugsDAO()

    def get_all(self):
        rows = self.dao.get_all()
        return rows

    def get_by_id(self, drug_id):
        return self.dao.get_by_id(drug_id)

    def create(self, data):
        return self.dao.create(data)

    def update(self, drug_id, data):
        return self.dao.update(drug_id, data)

    def delete(self, drug_id):
        return self.dao.delete(drug_id)

    def get_drugs_by_manufacturers(self):
        return self.dao.get_drugs_by_manufacturers()

    def get_drugs_with_ingredients(self):
        return self.dao.get_drugs_with_ingredients()

    def get_drugs_with_usages(self):
        return self.dao.get_drugs_with_usages()

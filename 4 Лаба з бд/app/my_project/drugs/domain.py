class Drug:
    def __init__(self, Id_drug=None, drug_name=None, category_id=None, manufacturer_id=None, description=None):
        self.Id_drug = Id_drug
        self.drug_name = drug_name
        self.category_id = category_id
        self.manufacturer_id = manufacturer_id
        self.description = description

    @classmethod
    def from_dict(cls, d):
        if not d: return None
        return cls(
            Id_drug=d.get("Id_drug"),
            drug_name=d.get("drug_name"),
            category_id=d.get("category_id"),
            manufacturer_id=d.get("manufacturer_id"),
            description=d.get("description")
        )

    def to_dict(self):
        return {
            "Id_drug": self.Id_drug,
            "drug_name": self.drug_name,
            "category_id": self.category_id,
            "manufacturer_id": self.manufacturer_id,
            "description": self.description
        }

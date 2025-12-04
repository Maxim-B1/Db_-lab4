class Supplier:
    def __init__(self, supplier_id=None, name=None, country=None, contact_info=None):
        self.supplier_id = supplier_id
        self.name = name
        self.country = country
        self.contact_info = contact_info

    @classmethod
    def from_dict(cls, d):
        if not d: return None
        return cls(
            supplier_id=d.get("supplier_id"),
            name=d.get("name"),
            country=d.get("country"),
            contact_info=d.get("contact_info")
        )

    def to_dict(self):
        return {
            "supplier_id": self.supplier_id,
            "name": self.name,
            "country": self.country,
            "contact_info": self.contact_info
        }

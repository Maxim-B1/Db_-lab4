class Manufacturer:
    def __init__(self, manufacturer_id=None, name=None, country=None, contact_info=None):
        self.manufacturer_id = manufacturer_id
        self.name = name
        self.country = country
        self.contact_info = contact_info

    @classmethod
    def from_dict(cls, d):
        if not d: return None
        return cls(
            manufacturer_id=d.get("manufacturer_id"),
            name=d.get("name"),
            country=d.get("country"),
            contact_info=d.get("contact_info")
        )

    def to_dict(self):
        return {
            "manufacturer_id": self.manufacturer_id,
            "name": self.name,
            "country": self.country,
            "contact_info": self.contact_info
        }

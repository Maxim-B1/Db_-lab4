class Package:
    def __init__(self, package_id=None, type=None, quantity=None):
        self.package_id = package_id
        self.type = type
        self.quantity = quantity

    @classmethod
    def from_dict(cls, d):
        if not d: return None
        return cls(package_id=d.get("package_id"), type=d.get("type"), quantity=d.get("quantity"))

    def to_dict(self):
        return {"package_id": self.package_id, "type": self.type, "quantity": self.quantity}

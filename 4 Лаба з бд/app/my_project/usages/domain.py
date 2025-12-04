class Usage:
    def __init__(self, usage_id=None, description=None):
        self.usage_id = usage_id
        self.description = description

    @classmethod
    def from_dict(cls, d):
        if not d: return None
        return cls(usage_id=d.get("usage_id"), description=d.get("description"))

    def to_dict(self):
        return {"usage_id": self.usage_id, "description": self.description}

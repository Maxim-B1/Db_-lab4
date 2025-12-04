class Category:
    def __init__(self, category_id=None, name=None, description=None):
        self.category_id = category_id
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, d):
        if not d:
            return None
        return cls(
            category_id=d.get("category_id"),
            name=d.get("name"),
            description=d.get("description")
        )

    def to_dict(self):
        return {
            "category_id": self.category_id,
            "name": self.name,
            "description": self.description
        }

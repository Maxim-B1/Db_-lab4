class Ingredient:
    def __init__(self, ingredient_id=None, name=None, description=None):
        self.ingredient_id = ingredient_id
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, d):
        if not d: return None
        return cls(
            ingredient_id=d.get("ingredient_id"),
            name=d.get("name"),
            description=d.get("description")
        )

    def to_dict(self):
        return {
            "ingredient_id": self.ingredient_id,
            "name": self.name,
            "description": self.description
        }

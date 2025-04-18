class Planet:
    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.description = description
        self.size = size
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "size": self.size
        }

planets = [
    Planet(1, "Flora", "Beautiful", "big"),
    Planet(2, "Renata", "Amazing", "big"),
    Planet(3, "Kira", "Fantastic", "medium"),
    Planet(4, "Darina", "Kind", "small")
]



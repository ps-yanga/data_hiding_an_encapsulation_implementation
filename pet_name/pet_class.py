import json

class Pet:
    def __init__(self):
        self._name=""
        self._animal_type=""
        self._age=0
        self._owner_name=""

    def set_name(self, name):
        self._name = name

    def set_animal_type(self, animal_type):
        self._animal_type = animal_type

    def set_age(self, age):
        self._age = age

    def set_owner_name(self, owner_name):
        self._owner_name = owner_name

    def get_name(self):
        return self._name

    def get_animal_type(self):
        return self._animal_type

    def get_age(self):
        return self._age

    def get_owner_name(self):
        return self._owner_name

    def to_dict(self):
        return {"owner_name": self._owner_name,
            "pet_name": self._name,
            "animal_type": self._animal_type,
            "age": self._age}

    def from_dict(self, data):
        self._owner_name = data.get("owner_name","")
        self._name = data.get("pet_name","")
        self._animal_type = data.get("animal_type", "")
        self._age = data.get("age", 0)

    @staticmethod
    def save_pets(pets_list, filename="pets_data.json"):
        try:
            with open(filename, 'w') as f:
                json.dump([pet.to_dict() for pet in pets_list], f, indent=4)
            print(f"{len(pets_list)} pet(s) saved to '{filename}'")
        except Exception as e:
            print(f" Error saving pets: {e}")

    @staticmethod
    def load_pets(filename="pets_data.json"):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            pets = []
            for pet_data in data:
                pet = Pet()
                pet.from_dict(pet_data)
                pets.append(pet)
            print(f"{len(pets)} pet(s) loaded from '{filename}'")
            return pets
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return []
        except Exception as e:
            print(f"✗ Error loading pets: {e}")
            return []
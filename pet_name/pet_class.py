class Pet:
    def __int__(self):
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
        self.__owner_name = owner_name

    def get_name(self):
        return self._name

    def get_animal_type(self):
        return self._animal_type

    def get_age(self):
        return self._age

    def get_owner_name(self):
        return self._owner_name
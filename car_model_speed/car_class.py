class Brand:
    def __init__(self, name, country):
        self._name = name
        self._country = country

    def get_name(self):
        return self._name

    def set_name(self, name):
        if name != "":
            self._name = name
        else:
            print("Error")

    def get_country(self):
        return self._country

    def set_country(self, country):
        if country != "":
            self._country = country
        else:
            print("Error")
    def display(self):
        print(f"Brand: {self._name}(Country: {self._country})")

class Car:
    def __init__(self, year_model,brand, model):
        self._year_model=year_model
        self._brand=brand
        self._model=model
        self._speed=0

    def get_year_model(self):
        return self._year_model

    def set_year_model(self,year_model):
        if year_model>0:
            self._year_model=year_model
        else:
            print("Error")

    def get_brand(self):
        return self._brand

    def set_brand(self,brand):
        if isinstance(brand, Brand):
            self._brand=brand
        else:
            print("Error")

    def get_model(self):
        return self._model

    def set_model(self,model):
        if model !="":
            self._model=model
        else:
            print("Error")

    def get_speed(self):
        return self._speed

    def set_speed(self,speed):
        if speed<0:
            print("Error")
            self._speed=0

    def accelerate(self):
        self._speed+=15

    def brake(self):
        self._speed-=5

    def display_info(self):
        print(f"Year: {self._year_model}, "
              f"\nModel: {self._model}, "
              f"\nBrand: {self._brand}, "
              f"\nInitial speed: {self._speed}")
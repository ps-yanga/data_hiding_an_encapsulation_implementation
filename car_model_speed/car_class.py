class Car:
    def __init__(self, year_model,make):
        self._year_model=year_model
        self._make=make
        self._speed=0

    def get_year_model(self):
        return self._year_model

    def set_year_model(self,year_model):
        if year_model>0:
            self._year_model=year_model
        else:
            print("Error")

    def set_make(self,make):
        if make !="":
            self._make=make
        else:
            print("Error")

    def get_make(self):
        return self._make

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

class Car:
    def __init__(self, year_model,make):
        self._year_model=year_model
        self._make=make
        self._speed=0

    def get_year_model(self):
        return self._year_model

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



mi_car=Car(2024, "Mazda")
print("Accelerating: ")
for i in range(5):
    mi_car.accelerate()
    print(f"Speed after acceleration {i+1}: {mi_car.get_speed()} mph")

print("\nBraking: ")
for i in range(5):
    mi_car.brake()
    print(f"Speed after braking {i+1}: {mi_car.get_speed()} mph")
from car_class import Car
mi_car=Car(2024, "Mazda")
print(f"Year Model: {mi_car.get_year_model()}"
      f"\nMake: {mi_car.get_make()}"
      f"\nInitial Speed: {mi_car.get_speed()}")


print("Accelerating: ")
for i in range(5):
    mi_car.accelerate()
    print(f"Speed after acceleration {i+1}: {mi_car.get_speed()} mph")

print("\nBraking: ")
for i in range(5):
    mi_car.brake()
    print(f"Speed after braking {i+1}: {mi_car.get_speed()} mph")
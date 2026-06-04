from fan_class_setting import Fan

fan1=Fan()
fan1.set_speed(Fan.fast)
fan1.set_radius(10)
fan1.set_color("yellow")
fan1.set_on(True)

fan2=Fan()
fan2.set_speed(Fan.medium)
fan2.set_radius(5)
fan2.set_color("blue")
fan2.set_on(False)

print("fan1: ")
print(f"   Speed: {fan1.get_speed()}")
print(f"   Radius: {fan1.get_radius()}")
print(f"   Color: {fan1.get_color()}")
print(f"   On: {fan1.get_on()}")

print("\nfan2: ")
print(f"   Speed: {fan2.get_speed()}")
print(f"   Radius: {fan2.get_radius()}")
print(f"   Color: {fan2.get_color()}")
print(f"   On: {fan2.get_on()}")

print("\nUsing __str__ method")
print(fan1)
print(fan2)
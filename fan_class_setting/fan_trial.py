from fan_class_setting import Fan

fan1=Fan()
fan1.speed=Fan.fast
fan1.radius=10
fan1.color="yellow"
fan1.on=True

fan2=Fan()
fan2.speed=Fan.medium
fan2.radius=5
fan2.color="blue"
fan2.on=False

print("fan 1: ")
print(f"   Speed: {fan1.speed}")
print(f"   Radius: {fan1.radius}")
print(f"   Color: {fan1.color}")
print(f"   On: {fan1.on}")

print("\nfan 2: ")
print(f"   Speed: {fan2.speed}")
print(f"   Radius: {fan2.radius}")
print(f"   Color: {fan2.color}")
print(f"   On: {fan2.on}")

print("\nTesting Validation")
print("Trying to set invalid speed(5): ")
fan1.speed=5

print("\nTrying to set invalid radius(-10): ")
fan1.radius=-10

print("\nTrying to set invalid on value('yes'): ")
fan1.on="yes"

print("\nUsing __str__ method")
print(fan1)
print(fan2)
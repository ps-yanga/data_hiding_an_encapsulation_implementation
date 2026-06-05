from car_class import Car, Brand

def display_menu():
    print("Car Management System")

def select_brand():
    print("\n Select a car brand")
    brands = {1: Brand("Land Rover", "United Kingdom"),
             2: Brand ("Nissan", "Japan"),
             3: Brand("Chevrolet", "United States"),
             4: Brand("Jeep", "United "),
             5: Brand("Mitsubishi", "Japan"),
             6: Brand("Mazda", "Japan"),
             7: Brand("Toyota", "Japan"),
             8: Brand("Ford", "United States"),
             9: Brand("Subaru", "Japan"),
             10: Brand("Ferrari", "Italy"),
             11: Brand("Maserati", "Italy"),
             12: Brand("Audi", "Germany")}

    for key, brand in brands.items():
        print(f"{key:2}: {brand.get_name()} ({brand.get_country()})")

    while True:
        try:
            choice = int(input("Choose brand (1-12): "))
            if choice not in range(1, 12):
                return brands[choice]
            else:
                print("Invalid, Select 1-12.")
        except ValueError:
            print("Enter a valid number.")

def select_model():
    print("\n Select a  model")
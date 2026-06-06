from car_class import Car, Brand

def display_menu():
    print("Car Management System")

def select_brand():
    print("\n Select a car brand")
    brands = {1: Brand("Land Rover", "United Kingdom"),
             2: Brand ("Nissan", "Japan"),
             3: Brand("Chevrolet", "United States"),
             4: Brand("Jeep", "United States"),
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
            if choice in range(1, 13):
                return brands[choice]
            else:
                print("Invalid, Select 1-12.")
        except ValueError:
            print("Enter a valid number.")

def select_model(brand_name):
    print(f"\n Select {brand_name} model")

    model_by_brand = {"Land Rover": { 1: "Range Rover Sport SV Edition Two 2026",
                                      2: "Land Rover Series 1 (1948)",
                                      3: "Range Rover Velar (2026)",
                                      4: "Bowler Wildcat (2000s)"},
                      "Nissan": {1: "Nissan GT-R (2024/2025)",
                                 2: "Nissan Skyline GT-R (2002)",
                                 3: "Nissan Z Nismo (2026)",
                                 4: "Nissan R390 GT1 (1998)",
                                 5: "Nissan Skyline 2000GT-R 'Hakosuka' (1971)"},
                      "Chevrolet": {1: "Chevrolet Camaro (2024)",
                                    2: "Corvette ZR1 (C8, 2026)",
                                    3: "Corvette Stingray Coupe (2026)",
                                    4: "Chevrolet Chevelle SS 454 (1970)"},
                      "Jeep": {1: "Jeep Wrangler Rubicon(2026)",
                               2: "Willy MB (1941)",
                               3: "Jeep Cherokee Chief Sport (1970s)",
                               4: "Jeep Hurricane Concept (2005)",
                               5: "Jeep Grand Cherokee Trackhawk (2021)"},
                      "Mitsubishi": {1: "Mistsubishi Lancer Evolution X Final Edition (2015)",
                                     2: "Mitsubishi Pajero Evolution (1997)",
                                     3: "Mitsubishi Eclipse GSX (1999)",
                                     4: "Mitsubishi HSR-II (1989 Concept)",
                                     5: "Mitsubishi Starion ESI-R (1988)"},
                      "Mazda": {1:"Mazda Furai (2008 Concept)",
                                2:"Mazda RX-7 FD3S (2002)",
                                3:"Mazda MX-5 Miata RF (2026)",
                                4:"Mazda 787B (1991)",
                                5:"Mazda RX-3 (1970s)"},
                      "Toyota": {
                          1: "Lexus LFA (2012)",
                          2: "Toyota 2000GT (1967)",
                          3: "Toyota GR Supra (2026)",
                          4: "Toyota GR Super Sport (Upcoming)",
                          5: "Toyota Celica Liftback 2000GT (1975)"},
                      "Ford": {1:"Ford GT (Second Gen, 2022)",
                               2:"Ford Mustang Shelby GT500 'Eleanor' (1967)",
                               3:"Ford Mustang Dark Horse (2026)",
                               4:"Ford GT Mk IV (2023)",
                               5:"Ford Torino Cobra Jet (1970)"},
                      "Subaru": {1: "Subaru WRX STI S209 (2019)",
                                 2: "Subaru Impreza 22B STI (1998)",
                                 3: "Subaru BRZ tS (2026)",
                                 4: "Subaru Project Midnight (2024/2025)",
                                 5: "Subaru SVX (1992)"},
                      "Ferrari": {
                          1: "Ferrari SF90 XX Stradale (2025)",
                          2: "Ferrari F40 (1987)",
                          3: "Ferrari Roma (2026)",
                          4: "Ferrari LaFerrari (2016)",
                          5: "Ferrari 550 Maranello (2001)"},
                      "Maserati": {
                          1: "Maserati MC20 Cielo (2026)",
                          2: "Maserati Ghibli SS (1970)",
                          3: "Maserati GranTurismo Trofeo (2026)",
                          4: "Maserati MC12 (2004)",
                          5: "Maserati Shamal (1990)"},
                      "Audi": {
                          1: "Audi R8 V10 Performance LMX (2023)",
                          2: "Audi Sport Quattro (1984)",
                          3: "Audi RS5 Coupe (2026)",
                          4: "Audi AI:RACE PB18 e-tron Concept",
                          5: "Audi RS6 Avant (2026)"}}

    models = model_by_brand.get(brand_name,{})

    for key, model in models.items():
        print(f"{key}: {model}")

    while True:
        try:
            choice=int(input(f"Choose a model (1-{len(models)}): "))
            if choice in models:
                return models[choice]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid choice. Please try again.")

def acceleration_braking(car):
    print("\nAccelerating: ")
    for i in range(5):
        car.accelerate()
        print(f"Speed after acceleration {i + 1}: {car.get_speed()} mph")

    print("\nBraking: ")
    for i in range(5):
        car.brake()
        print(f"Speed after braking {i + 1}: {car.get_speed()} mph")

    print("\n" + "=" * 60)
    print(f"Final Speed: {car.get_speed()} mph")
    print("=" * 60)

def main():
    while True:
        display_menu()
        print("\n1. Create a new car")
        print("2. Exit")

        choice = input("Choose option (1-2): ")

        if choice == "1":
            brand = select_brand()
            model = select_model(brand.get_name())

            car = Car("", brand, model)

            print("CAR CREATED SUCCESSFULLY!")
            print(f"Brand: {brand.get_name()} ({brand.get_country()})")
            print(f"Model: {model}")
            print(f"Initial Speed: {car.get_speed()} mph")
            acceleration_braking(car)


        elif choice == "2":
            print("Thank you for using Car Management System!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1 or 2.")


if __name__ == "__main__":
    main()
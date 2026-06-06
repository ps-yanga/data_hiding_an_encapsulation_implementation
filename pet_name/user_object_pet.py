from pet_class import Pet

def pawrents():
    pets_list = []

    print("Pet Information System\n")

    while True:
        print("\n1. Add New Pet")
        print("2. View All Pets")
        print("3. Load Saved Pets")
        print("4. Save All Pets")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ")

        if choice == "1":
            pet = Pet()
            owner_name = input("Enter owner name: ")
            pet.set_owner_name(owner_name)
            name = input("Enter pet name: ")
            pet.set_name(name)
            animal_type = input("Enter animal type: ")
            pet.set_animal_type(animal_type)
            try:
                age = int(input("Enter pet age: "))
                pet.set_age(age)
            except ValueError:
                pet.set_age(0)
            pets_list.append(pet)
            print("✓ Pet added!")

        elif choice == "2":
            if not pets_list:
                print("No pets in the system.")
            else:
                print("\n=== All Pets ===")
                for i, pet in enumerate(pets_list, 1):
                    print(f"\n{i}. Owner: {pet.get_owner_name()}")
                    print(f"   Pet: {pet.get_name()}")
                    print(f"   Type: {pet.get_animal_type()}")
                    print(f"   Age: {pet.get_age()}")

        elif choice == "3":
            pets_list = load_pets()

        elif choice == "4":
            if pets_list:
                save_pets(pets_list)
            else:
                print("No pets to save.")

        elif choice == "5":
            print("Goodbye!")
            break


if __name__ == "__main__":
    pawrents()
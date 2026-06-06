from pet_class import Pet

def pawrents():
    pet = Pet()

    print("Pet Information System")

    owner_name=input("Enter name of the pet owner: ")
    pet.set_owner_name(owner_name)

    name=input("Enter name of the pet name: ")
    pet.set_name(name)

    animal_type=input("Enter animal type (e.g. Dog, Cat, Bird...,: ")
    pet.set_animal_type(animal_type)

    try:
        age=int(input("Enter age of your pet: "))
        pet.set_age(age)
    except ValueError:
        print("Invalid age")
        pet.set_age(0)

    print("Pet Information")
    print(f"\nOwner Name: {pet.get_owner_name()}"
          f"\nName: {pet.get_name()}"
          f"\nType: {pet.get_animal_type()}"
          f"\nAge: {pet.get_age()}")

if __name__ == "__main__":
    pawrents()
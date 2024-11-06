
# farm.py

class Farm:
    def __init__(self):
        self.crops = []
        self.animals = []

    def add_crop(self):
        crop_name = input("Enter the name of the crop: ")
        self.crops.append(crop_name)
        print(f"Added crop: {crop_name}")

    def add_animal(self):
        animal_name = input("Enter the name of the animal: ")
        self.animals.append(animal_name)
        print(f"Added animal: {animal_name}")

    def show_farm_status(self):
        print("\nFarm Status:")
        print("Crops:", ", ".join(self.crops) if self.crops else "No crops")
        print("Animals:", ", ".join(self.animals) if self.animals else "No animals")


def main():
    farm = Farm()
    
    while True:
        print("\nChoose an option:")
        print("1. Add a crop")
        print("2. Add an animal")
        print("3. Show farm status")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            farm.add_crop()
        elif choice == "2":
            farm.add_animal()
        elif choice == "3":
            farm.show_farm_status()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()

# Assignment 1: Classes, Inheritance, and Polymorphism

# --- Activity 1: Create your own class ---
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def details(self):
        print(f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB")

# Inheritance Example
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu_power):
        super().__init__(brand, model, storage)  # Call parent constructor
        self.gpu_power = gpu_power

    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with GPU power {self.gpu_power}!")

# --- Activity 2: Polymorphism challenge ---
class Animal:
    def move(self):
        print("Animals can move in different ways.")

class Dog(Animal):
    def move(self):
        print("Dog is running on four legs.")

class Bird(Animal):
    def move(self):
        print("Bird is flying in the sky.")

class Fish(Animal):
    def move(self):
        print("Fish is swimming in the water.")

# --- Testing the code ---
if __name__ == "__main__":
    # Activity 1 test
    phone1 = Smartphone("Samsung", "Galaxy S23", 256)
    phone1.details()
    phone1.call("0712345678")

    gaming_phone = GamingPhone("Asus", "ROG Phone 7", 512, "High-End GPU")
    gaming_phone.details()
    gaming_phone.play_game("Call of Duty")

    print("\n--- Polymorphism Demo ---")
    animals = [Dog(), Bird(), Fish()]
    for animal in animals:
        animal.move()


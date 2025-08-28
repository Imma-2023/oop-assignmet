# Python OOP Assignment 1

This project contains solutions for **Assignment 1: Object-Oriented Programming (OOP)**.  
It demonstrates the use of **classes, constructors, inheritance, and polymorphism** in Python.

---

## 📌 Activity 1: Design Your Own Class
- Created a `Smartphone` class with attributes and methods.
- Added an inherited class `GamingPhone` to demonstrate **inheritance**.
- Used constructors to initialize objects with unique values.

### Example
```python
phone1 = Smartphone("Samsung", "Galaxy S23", 256)
phone1.details()
phone1.call("0712345678")

gaming_phone = GamingPhone("Asus", "ROG Phone 7", 512, "High-End GPU")
gaming_phone.details()
gaming_phone.play_game("Call of Duty")



animals = [Dog(), Bird(), Fish()]
for animal in animals:
    animal.move()

Dog is running on four legs.
Bird is flying in the sky.
Fish is swimming in the water.

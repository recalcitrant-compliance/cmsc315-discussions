"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


class Guitar:
    brandName = "Fender"
    numberOfStrings = 6
    stringTuning = "EADGBE"

    def __init__(self, owner, year, body_style):
        self.owner = owner
        self.year = year
        self.body_style = body_style

    def display_info(self):
        print(
            f"Brand: {self.brandName}, Strings: {self.numberOfStrings}, Tuning: {self.stringTuning}"
        )


class ElectricGuitar(Guitar):
    modelName = "Stratocaster"
    pickupConfiguration = "Single Coil"
    numberOfSoundControls = 3

    def __init__(self, owner, year, body_style, amplifier, color):
        super().__init__(owner, year, body_style)
        self.amplifier = amplifier
        self.color = color
        self.features = ["volume", "tone", "bridge"]

    def display_info(self):
        print(
            f"Brand: {self.brandName}, Model: {self.modelName}, Strings: {self.numberOfStrings}, "
            f"Pickups: {self.pickupConfiguration}, Tuning: {self.stringTuning}, "
            f"Controls: {self.numberOfSoundControls}"
        )

    def play(self):
        print(f"{self.owner} is playing the {self.brandName} {self.modelName} through a {self.amplifier} amp.")


def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    guitar_1 = ElectricGuitar("Alice", 2020, "Solid Body", "Marshall", "Sunburst")
    guitar_2 = ElectricGuitar("Bob", 2022, "Solid Body", "Fender", "Black")

    print(f"Class variable through class: {ElectricGuitar.brandName}")
    print(f"Class variable through object: {guitar_1.brandName}")

    guitar_1.custom_pickguard = "Pearloid"

    print("\nObject 1 namespace (__dict__):")
    print(guitar_1.__dict__)

    print("\nObject 2 namespace (__dict__):")
    print(guitar_2.__dict__)

    print("\nClass namespace information:")
    class_namespace = {
        key: value
        for key, value in ElectricGuitar.__dict__.items()
        if not key.startswith("__")
    }
    print(class_namespace)


def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = ElectricGuitar("Charlie", 2021, "Solid Body", "Orange", "Red")
    original.features = ["volume", "tone", ["neck pickup", "bridge pickup"]]

    # Shallow copy copies the outer object, but nested mutable objects are shared.
    shallow_copy = copy(original)

    # Deep copy copies the outer object and all nested mutable objects recursively.
    deep_copy = deepcopy(original)

    original.features[2].append("middle pickup")

    print("Original object:")
    print(original.__dict__)

    print("\nShallow copy:")
    print(shallow_copy.__dict__)

    print("\nDeep copy:")
    print(deep_copy.__dict__)


def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Guitar Demonstration ===")
    Guitar.brandName = "Fender"
    guitar_one = Guitar("Jordan", 2018, "Acoustic")
    guitar_one.display_info()

    Guitar.brandName = "Gibson"
    guitar_two = Guitar("Taylor", 2019, "Acoustic")
    guitar_two.display_info()

    print("\n=== Electric Guitar Demonstration ===")
    ElectricGuitar.brandName = "Fender"
    ElectricGuitar.modelName = "Stratocaster"
    ElectricGuitar.pickupConfiguration = "Single Coil"
    ElectricGuitar.numberOfSoundControls = 3
    electric_one = ElectricGuitar("Sam", 2022, "Solid Body", "Marshall", "Blue")
    electric_one.display_info()

    ElectricGuitar.brandName = "Gibson"
    ElectricGuitar.modelName = "SG"
    ElectricGuitar.pickupConfiguration = "Humbucker"
    ElectricGuitar.numberOfSoundControls = 4
    electric_two = ElectricGuitar("Casey", 2023, "Solid Body", "Orange", "Cherry")
    electric_two.display_info()

    print("\n=== Inheritance Demonstration ===")
    guitar_one.display_info()
    electric_one.play()

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
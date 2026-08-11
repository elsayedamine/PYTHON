class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age

    def show(self):
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self):
        self._height = round(self._height + 0.6, 1)

    def age(self):
        self._age += 1

    def set_height(self, height):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        self._height = height
        return True

    def set_age(self, age):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        self._age = age
        return True

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self):
        self._bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self._color}")
        print(f"{self.name} is blooming beautifully!") if (self._bloomed) \
            else print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade "
            f"of {self._height:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide."
        )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def age(self):
        super().age()
        self._nutritional_value += 1

    def show(self):
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()

    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()

    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()

    print("[make tomato grow and age for 20 days]")

    for _ in range(20):
        tomato.grow()
        tomato.age()

    tomato.show()
    print(f"Nutritional value: {tomato._nutritional_value}")

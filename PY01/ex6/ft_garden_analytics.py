# staticmethod
# classmethod
# isinstance
# cls vs self (self gives you the object/ cls gives you the class)

class Plant:
    class Stats:
        def __init__(self):
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self):
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, "
                f"{self._show_count} show"
            )

    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age
        self._stats = Plant.Stats()

    def show(self):
        self._stats._show_count += 1
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self):
        self._stats._grow_count += 1
        self._height = round(self._height + 0.6, 1)

    def age(self):
        self._stats._age_count += 1
        self._age += 1

    @staticmethod
    def is_older_than_year(days: int):
        return days > 365
    # is_older_than_year = staticmethod(is_older_than_year)

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)
    # create_anonymous = classmethod(create_anonymous)
    # getters and setters

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
    class TreeStats:
        def __init__(self):
            self._shade_count = 0

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._stats._show_count += 1
        self._tree_stats = Tree.TreeStats()

    def produce_shade(self):
        self._tree_stats._shade_count += 1
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


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self._seeds = 0

    def bloom(self):
        super().bloom()
        self._seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self._seeds}")


def display_stats(plant):
    print(f"[statistics for {plant.name}]")
    plant._stats.display()

    if isinstance(plant, Tree):
        print(f"{plant._tree_stats._shade_count} shade")


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> "
          f"{Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> "
          f"{Plant.is_older_than_year(400)}")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)

    print("0 shade")

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()

    for _ in range(20):
        sunflower.age()

    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_stats(anonymous)

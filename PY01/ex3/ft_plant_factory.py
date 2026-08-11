class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self._age = age

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

    def grow(self):
        self.height = round(self.height + 0.6, 1)

    def age(self):
        self._age += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    Red = Plant("Red", 26.0, 30)
    Violet = Plant("Violet", 27.0, 30)
    Blue = Plant("Blue", 28.0, 30)
    magenta = Plant("magenta", 29.0, 30)

    print("=== Garden Plant Growth ===")
    rose.show()
    Red.show()
    Violet.show()
    Blue.show()
    magenta.show()

    start_height = rose.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()

    print(f"Growth this week: {round(rose.height - start_height, 1)}cm")

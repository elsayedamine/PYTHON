class Plant:
    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")
    def grow(self):
        self.height = round(self.height + 0.6, 1)
    def age(self):
        self._age += 1

if __name__ == "__main__":
    rose = Plant()

    rose.name = "Rose"
    rose.height = 25.0
    rose._age = 30

    print("=== Garden Plant Growth ===")
    rose.show()

    start_height = rose.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()

    print(f"Growth this week: {round(rose.height - start_height, 1)}cm")
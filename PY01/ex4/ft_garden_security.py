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


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print("Plant created:", end=" ")
    rose.show()

    if rose.set_height(25):
        print(f"Height updated: {rose.get_height():.0f}cm")
    else:
        print("Height update rejected")

    if rose.set_age(30):
        print(f"Age updated: {rose.get_age()} days")
    else:
        print("Age update rejected")

    if rose.set_height(-5):
        print(f"Height updated: {rose.get_height():.0f}cm")
    else:
        print("Height update rejected")

    if rose.set_age(-10):
        print(f"Age updated: {rose.get_age()} days")
    else:
        print("Age update rejected")

    print("Current state:", end=" ")
    rose.show()

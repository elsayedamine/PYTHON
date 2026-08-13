import math


def get_player_pos():
    while True:
        try:
            vals = input("Enter new coordinates as \
                         floats in format 'x,y,z': ").split(",")
            if len(vals) != 3:
                raise ValueError("Invalid syntax")
            crd: tuple[float, float, float] = (float(vals[0]),
                                               float(vals[1]), float(vals[2]))
            return crd
        except ValueError as e:
            print(e)


def main():
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    c1 = get_player_pos()
    print(f"Got a first tuple: {c1}")
    print(f"It includes: X={c1[0]}, Y={c1[1]}, Z={c1[2]}")
    print(f"Distance to center: {math.sqrt(c1[0]**2 +
                                           c1[1]**2 + c1[2]**2):.4f}\n")

    print("\nGet a second set of coordinates")
    c2 = get_player_pos()
    dist = math.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2 +
                     (c2[2] - c1[2])**2)
    print(f"Distance between the 2 sets of coordinates: {dist:.4f}")


if __name__ == "__main__":
    main()

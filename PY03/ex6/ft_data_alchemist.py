# from itertools import zip_longest as zp
import random


players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
           'Gregory', 'john', 'kevin', 'Liam']
scores = [random.randint(0, 700) for _ in range(len(players))]


def main():
    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {players}")
    capitalized: list[str] = [player.capitalize() for player in players]
    only_capitalized: list[str] = [player for player in players
                                   if (player[0].isupper())]
    print(f"New list with all names capitalized: {capitalized}")
    print(f"New list of capitalized names only: {only_capitalized}\n")

    data: dict[str, int] = {key: val for key, val in zip(capitalized, scores)}
    average: float = sum(data.values()) / len(data)
    print(f"Score dict: {data}")
    print(f"Score average is {average:.2f}")
    highest: dict[str, int] = {key: val for key, val
                               in data.items() if val > average}
    print(f"High score: {highest}")
    return


if __name__ == "__main__":
    main()

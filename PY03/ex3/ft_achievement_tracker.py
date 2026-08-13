import random


ACHIEVEMENTS = [
    "First Steps", "World Savior", "Master Explorer",
    "Boss Slayer", "Crafting Genius", "Strategist",
    "Speed Runner", "Survivor", "Treasure Hunter",
    "Unstoppable", "Collector Supreme", "Untouchable",
    "Sharp Mind", "Hidden Path Finder"
]


def gen_player_achievements():
    # returns a rand int btwm a and b, inclusive.
    n = random.randint(3, 8)
    # randomly chooses n different elements from a sequence
    return set(random.sample(ACHIEVEMENTS, n))
    # set create a set of unique elets (removes dups)


def main():
    print("=== Achievement Tracker System ===")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    # union bayna like math (remove dups)
    all_achievements = alice.union(bob, charlie, dylan)
    # same for intersect
    common = alice.intersection(bob, charlie, dylan)

    print(f"All distinct achievements: {all_achievements}")
    print(f"Common achievements: {common}")

    # returns elets that are in the first set but not in the others.
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")

    print(f"Alice is missing: {all_achievements.difference(alice)}")
    print(f"Bob is missing: {all_achievements.difference(bob)}")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}")


if __name__ == "__main__":
    main()

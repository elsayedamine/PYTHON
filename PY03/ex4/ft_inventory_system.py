import sys


def main():
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]
        pair = arg.split(":")
        if (len(pair) != 2):
            print(f"Error - invalid parameter '{arg}'")
            continue
        if (pair[0] in inventory):
            print(f"Redundant item '{pair[0]}' - discarding")
            continue
        try:
            val = int(pair[1])
            inventory[pair[0]] = val
        except ValueError as v:
            print(f"Quantity error for '{pair[0]}': {v}")
    if not inventory:
        print("Empty inventory")
        print("\tUsage: <item_name1>:<quantity1> <item_name2>:<quantity2> ...")
        return
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    total_quantity: int = sum(list(inventory.values()))
    print(f"Total quantity of the {len(inventory)} quantity: {total_quantity}")
    for item, quant in inventory.items():
        print(f"Item {item} represents {(quant / total_quantity * 100):.1f}%")
    most_abundant: int = max(inventory.values())
    least_abundant: int = min(inventory.values())

    # print(f"Item most abundant: {next(iter([key
    # for key, value in inventory.items() if value == most_abundant]))}
    # with quantity {most_abundant}")
    # print(f"Item least abundant: {next(iter([key
    # for key, value in inventory.items() if value == least_abundant]))}
    # with quantity {least_abundant}")

    Item_most_abundant: str = [key for key, value in inventory.items()
                               if value == most_abundant][0]
    Item_least_abundant: str = [key for key, value in inventory.items()
                                if value == least_abundant][0]
    print(f"Item most abundant: {Item_most_abundant}"
          "with quantity {most_abundant}")
    print(f"Item least abundant: {Item_least_abundant}"
          "with quantity {least_abundant}")
    inventory.update({"katana": 3})  # using dict
    inventory.update(nenchaku=3, reaper=1)  # using kwargs
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()

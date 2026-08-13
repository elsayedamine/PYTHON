import sys


def main():
    # print(sys.argv)
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if (len(sys.argv) == 1):
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        # i can also use slicing sys.argv[1:]
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()

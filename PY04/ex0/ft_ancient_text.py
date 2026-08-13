import sys
import typing


def main():
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file: typing.IO[str] | None = None
    try:
        # typing.IO[str]: a type annotation to let u know
        # ur dealing with i/o object dealing with strs
        file = open(filename)
        content = file.read()

        print("---\n")
        print(content, end="")
        print("\n\n---")

    except Exception as error:
        print(f"Error opening file '{filename}': {error}")

    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()

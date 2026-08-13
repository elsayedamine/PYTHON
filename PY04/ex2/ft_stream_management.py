import sys
import typing


def main():
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file: typing.IO[str] | None = None

    try:
        file = open(filename)
        content = file.read()

        print("---")
        print(content, end="")
        print("---")

    except Exception as error:
        print(f"[STDERR] Error opening file '{filename}': {error}",
              file=sys.stderr)
        return

    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed.")

    print("Transform data:")
    transformed = "\n".join(
        line + "#" for line in content.splitlines()
    )
    print("---")
    print(transformed)
    print("---")

    print("Enter new file name (or empty): ", end="", flush=True)
    new_filename = sys.stdin.readline().strip()

    if not new_filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")

    output: typing.IO[str] | None = None

    try:
        output = open(new_filename, "w")
        output.write(transformed)
        print(f"Data saved in file '{new_filename}'.")

    except Exception as error:
        print(f"[STDERR] Error opening file '{new_filename}': {error}",
              file=sys.stderr)
        print("Data not saved.")

    finally:
        if output is not None:
            output.close()


if __name__ == "__main__":
    main()

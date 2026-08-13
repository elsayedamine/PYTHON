def secure_archive(
    filename: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as file:
                return (True, file.read())
        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
        else:
            return (False, "Invalid action")
    except Exception as error:
        return (False, str(error))


def main():
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    success, data = secure_archive("ancient_fragment.txt")
    print((success, data))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "write", data))


if __name__ == "__main__":
    main()


# # in this excercise we use with
# # You can create your own context manager:

# class Resource:
#     def __enter__(self):
#         print("Acquiring resource")
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Cleaning up")

# # Then use the with keyword
# with Resource() as resource:
#     print("Using resource")

# # Even if :
# with Resource() as resource:
#     raise Exception()

# # the __exit__() method still gets called

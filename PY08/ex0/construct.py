import sys
import site
import os


def main():
    outside = "You're still plugged in"
    inside = "Welcome to the construct"
    status = outside if sys.base_prefix == sys.prefix else inside
    print(f"MATRIX STATUS: {status}\n")
    print(f"Current Python: {sys.executable}")
    venv = "None detected" if sys.base_prefix == sys.prefix else sys.prefix
    print(f"Virtual Environment: {os.path.basename(venv)}")
    if sys.base_prefix != sys.prefix:
        print(f"Environment Path: {sys.prefix}")
    warning = "\nWARNING: You're in the global environment!\n\
                The machines can see everything you install.\n"
    success = "\nSUCCESS: You're in an isolated environment!\n\
                Safe to install packages without affecting the global \
                    system.\n"
    print(f"{warning if sys.base_prefix == sys.prefix else success}")
    if sys.base_prefix == sys.prefix:
        print("To enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\\Scripts\\activate # On Windows\n\n"
              "Then run this program again.")
    if sys.base_prefix != sys.prefix:
        print("Package installation path:")
        print(f"{site.getsitepackages()[0]}")


if __name__ == "__main__":
    main()

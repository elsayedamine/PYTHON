import importlib


REQUIRED_PACKAGES = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib": "Visualization",
}


def check_dependencies():
    print("Checking dependencies:")

    missing = []

    for package, purpose in REQUIRED_PACKAGES.items():
        try:
            module = importlib.import_module(package)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {package} ({version}) - {purpose} ready")
        except ImportError:
            print(f"[MISSING] {package} - {purpose}")
            missing.append(package)

    return missing


def show_installation_instructions(missing):
    if not missing:
        return

    print("\nMissing dependencies detected.")

    print("\nUsing pip:")
    print("pip install -r requirements.txt")

    print("\nUsing Poetry:")
    print("poetry install")
    print("poetry run python loading.py")


def compare_versions():
    print("\nINSTALLED PACKAGE VERSIONS")

    for package in REQUIRED_PACKAGES:
        try:
            module = importlib.import_module(package)
            version = getattr(module, "__version__", "unknown")
            print(f"{package:<12} installed: {version}")
        except ImportError:
            print(f"{package:<12} installed: NOT FOUND")


def compare_package_managers():
    print("\n" + "=" * 50)
    print("DEPENDENCY MANAGEMENT COMPARISON")
    print("=" * 50)

    print("\npip:")
    print("  Configuration : requirements.txt")
    print("  Installation  : pip install -r requirements.txt")
    print("  Environment    : does not manage the project itself")
    print("  Lock file      : not provided by requirements.txt")

    print("\nPoetry:")
    print("  Configuration : pyproject.toml")
    print("  Installation  : poetry install")
    print("  Environment    : manages a project virtual environment")
    print("  Lock file      : poetry.lock")
    print("  Reproducible  : exact dependency resolution via poetry.lock")

    print("\nKey difference:")
    print("  pip installs packages.")
    print("  Poetry manages the project's dependencies and environment.")
    print("=" * 50)


def analyze_data():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")

    data = np.random.normal(100, 15, 1000)

    df = pd.DataFrame({"matrix_signal": data})  # converts data into a table

    print(f"Processing {len(df)} data points...")
    print("Generating visualization...")

    plt.figure(figsize=(10, 6))          # Create a 10×6 inch figure (canvas)
    plt.plot(df["matrix_signal"])     # Plot the matrix_signal values as a line
    plt.title("Matrix Signal Analysis")  # Set the graph title
    plt.xlabel("Data Point")             # Label the X-axis
    plt.ylabel("Signal")                 # Label the Y-axis
    plt.tight_layout()                   # Automatically adjust spacing
    plt.savefig("matrix_analysis.png")   # Save the graph as a PNG image
    plt.close()

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    print("LOADING STATUS: Loading programs...")

    missing = check_dependencies()

    if missing:
        show_installation_instructions(missing)
        return

    compare_versions()

    compare_package_managers()

    analyze_data()


if __name__ == "__main__":
    main()

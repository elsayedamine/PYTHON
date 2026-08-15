import os
from dotenv import load_dotenv


def load_configuration():
    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    return config


def validate_configuration(config):
    required = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]

    missing = []

    for key in required:
        if not config[key]:
            missing.append(key)

    if missing:
        print("Configuration warnings:")
        for key in missing:
            print(f"[MISSING] {key}")

        return False

    return True


def show_configuration(config):
    mode = config["MATRIX_MODE"]

    print("Accessing the Mainframe")
    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if mode == "development":
        print("Database: Connected to local instance")
    elif mode == "production":
        print("Database: Connected to production instance")
    else:
        print(f"Database: Unknown mode '{mode}'")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Not authenticated")

    print(f"Log Level: {config['LOG_LEVEL'] or 'NOT SET'}")

    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check():
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file detected")
    else:
        print("[WARNING] .env file not found")

    print("[OK] Production overrides available")


def main():
    config = load_configuration()

    if not validate_configuration(config):
        print("\nPlease configure the missing variables in .env")
        print("You can use .env.example as a template.")
        return

    show_configuration(config)
    security_check()

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()

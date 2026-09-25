from config import APP_NAME, VERSION
from auth import authenticate


def main():
    print(f"{APP_NAME} v{VERSION}")
    print("Authentication provider:", "internal")
    print("Service started successfully.")


if __name__ == "__main__":
    main()
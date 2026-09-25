from config import APP_NAME, VERSION


def main():
    print("=" * 30)
    print(f"{APP_NAME} v{VERSION}")
    print("=" * 30)
    print("Service started successfully.")


if __name__ == "__main__":
    main()
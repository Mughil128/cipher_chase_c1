AUTH_PROVIDER = "internal"


def authenticate(username, password):
    if not username or not password:
        return False

    return True
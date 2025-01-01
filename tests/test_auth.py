from auth.auth import Auth


def test_authentication():
    auth = Auth()
    try:
        auth_response = auth.authenticate()
        print("Authentication successful:", auth_response)
    except Exception as e:
        print("Error during authentication:", e)

if __name__ == "__main__":
    test_authentication()



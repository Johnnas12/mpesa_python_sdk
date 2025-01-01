from mpesa import Mpesa

PAYLOAD = {
    "ShortCode": "101010",
    "ResponseType": "Completed",
    "CommandID": "RegisterURL",
    "ConfirmationURL": "http://mydomain.com/c2b/confirmation",
    "ValidationURL": "http://mydomai.com/c2b/validation"
}

def test_register_url():
    register_url = Mpesa()
    response = register_url.register_url(PAYLOAD)
    if response:
        print("Response:", response)

if __name__ == "__main__":
    test_register_url(test_register_url())

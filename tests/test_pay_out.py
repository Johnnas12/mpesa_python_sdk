from auth.auth import Auth
from pay_out.pay_out import PayOut

AUTH_URL = "https://apisandbox.safaricom.et/v1/token/generate?grant_type=client_credentials"

def test_pay_out():
    auth = Auth()
    try:
        auth_result = auth.authenticate()
        print("Authentication successful:", auth_result)
        if auth.access_token:
            pay_out = PayOut(auth)
            pay_out_data = {
                        "InitiatorName": "testapi",
                        "SecurityCredential": "iSHJEgQYt3xidNVJ7lbXZqRXUlBqpM/ytL5incRQISaAYX/daObQopdHWiSVXJvexSoYCt9mmb6+TiikmTrGZm5fbaT1BeuPKDF9NFpOLG3n3hUZE2s5wNJvFxD3sM62cBdCQulFquFBc0CwHpq/K2cU1MN8lahvYp+vHnmGODogMBDk8/5Q+5CuRRFNRIt50xM0r10kUHVeWgUa71H6oK2RqXnog4EPTnanMlswz7N3J8jeIKzgGUwnJA8va5CvuNWu2B2L1cAm9g6pGribcgFZ2sgzByJpRWBkfntjGgzsYXh+K3fPZmxWyTQi7TscSvujH1EaS7JxvCIWMM3K0Q==",
                        "Occassion": "Disbursement",
                        "CommandID": "BusinessPayment",
                        "PartyA": "101010",
                        "PartyB": "251700100100",
                        "Remarks": "Test B2C",
                        "Amount": 12,
                        "QueueTimeOutURL": "https://mydomain.com/b2c/timeout",
                        "ResultURL": "https://mydomain.com/b2c/result"
            }
            result = pay_out.pay_out(pay_out_data)
            if result:
                print("pay out successful:", result)
            else:
                print("pay out failed.")
        else:
            print("No token found. Authentication failed.")

    except Exception as e:
        print("Error during authentication or pay out:", e)

if __name__ == "__main__":
    test_pay_out()
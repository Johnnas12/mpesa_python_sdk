from mpesa.api import Mpesa
from auth.auth import Auth
import asyncio

AUTH_URL = "https://apisandbox.safaricom.et/v1/token/generate?grant_type=client_credentials"

PAYMENT_PAYLOAD = {
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

async def test_pay_out():
    auth = Auth(base_url = AUTH_URL)
    token_data = await auth.authenticate()

    if token_data:
        print("Authentication successful:", token_data)
        mpesa = Mpesa(auth=auth)

        try:
            response = await mpesa.pay_out(PAYMENT_PAYLOAD)
            if response:
                print('payment response:', response)
            else:
                print("payment failed.")
        except Exception as e:
            print("Error during payment testing:", e)
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    asyncio.run(test_pay_out())



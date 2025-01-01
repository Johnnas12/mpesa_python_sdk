This is not offical SDK for mpesa API

# Introduction
This is comprensihive guide on how to use mpessa payment gateway SDK in your appilication. M-PESA is a mobile money transfer service that allows users to send and receive money, pay bills, and shop cashlessly in Ethiopia 
# Installation
```
pip install mpesa-python
```
# Usage Examples
## Authentication
```
from auth import Auth

def test_authentication():
    auth = Auth()
    try:
        auth_response = auth.authenticate()
        print("Authentication successful:", auth_response)
    except Exception as e:
        print("Error during authentication:", e)

if __name__ == "__main__":
    test_authentication()

```
## STK PUSH Usage Example
```
import asyncio
from auth import Auth
from mpesa import Mpesa

# u can define your payload here this is just dummy data i used for testing
PAYMENT_PAYLOAD = {
            "MerchantRequestID": "SFC-Testing",
            "BusinessShortCode": "554433",
            "Password": "123",
            "Timestamp": "20160216165627",
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "10.00",
            "PartyA": "251700404789",
            "PartyB": "554433",
            "PhoneNumber": "251700404789",
            "TransactionDesc": "Monthly Unlimited Package via Chatbot",
            "CallBackURL": "https://....",
            "AccountReference": "DATA",
            "ReferenceData": [
            {
            "Key": "BundleName",
            "Value": "Monthly Unlimited Bundle"
            },
            {
            "Key": "BundleType",
            "Value": "Self"
            },
            {
            "Key": "TINNumber",
            "Value": "89234093223"
            }
            ]
}

async def test_payment():
    # Authenticate first
    auth = Auth()
    token_data = auth.authenticate()
    
    if token_data:
        print("Authenticati4on successful:", token_data)
        
        # Create an instance of Mpesa with the authenticated token
        mpesa = Mpesa(auth=auth)
        # Test the ussd_push_checkout method
        try:
            response = mpesa.stk_push(PAYMENT_PAYLOAD)
            if response:
                print("Payment response:", response)
            else:
                print("Payment failed.")
        except Exception as e:
            print("Error during payment testing:", e)
    else:
        print("Authentication failed.")


if __name__ == "__main__":
    asyncio.run(test_payment())
```

## Pay Out Example
```
from mpesa import Mpesa
from auth import Auth

PAYMENT_PAYLOAD = {
        "InitiatorName": "testapi",
        "SecurityCredential": "YOUR_CREDENTIALS",
        "Occassion": "Disbursement",
        "CommandID": "BusinessPayment",
        "PartyA": "101010",
        "PartyB": "251700100100",
        "Remarks": "Test B2C",
        "Amount": 12,
        "QueueTimeOutURL": "https://mydomain.com/b2c/timeout",
        "ResultURL": "https://mydomain.com/b2c/result"
}

def test_pay_out():
    auth = Auth()
    token_data =  auth.authenticate()

    if token_data:
        print("Authentication successful:", token_data)
        mpesa = Mpesa(auth=auth)
        try:
            response = mpesa.pay_out(PAYMENT_PAYLOAD)
            if response:
                print('payment response:', response)
            else:
                print("payment failed.")
        except Exception as e:
            print("Error during payment testing:", e)
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    test_pay_out()
```

## Register URL Example
```
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
```

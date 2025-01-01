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

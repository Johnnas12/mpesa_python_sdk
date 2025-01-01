import asyncio
from auth.auth import Auth
from mpesa.api import Mpesa

# Set the test base URL for authentication
BASE_URL = "https://apisandbox.safaricom.et/v1/token/generate?grant_type=client_credentials"

# Set up the payment payload
PAYMENT_PAYLOAD = {
            "MerchantRequestID": "SFC-Testing-9146-4216-9455-e3947ac570fc",
            "BusinessShortCode": "554433",
            "Password": "123",
            "Timestamp": "20160216165627",
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "10.00",
            "PartyA": "251700404789",
            "PartyB": "554433",
            "PhoneNumber": "251700404789",
            "TransactionDesc": "Monthly Unlimited Package via Chatbot",
            "CallBackURL": "https://apigee-listener.oat.mpesa.safaricomet.net/api/ussd-push/result",
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
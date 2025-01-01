from auth.auth import Auth
from accept_payment_customer_initiated.customer_initiated_payement import CustomerInitiatedPayment

# Set the test base URL
BASE_URL = "https://apisandbox.safaricom.et/v1/token/generate?grant_type=client_credentials"  # Replace with the actual test endpoint base URL

def test_customer_initiated_payment():
    # Authenticate first
    auth = Auth(base_url=BASE_URL)
    try:
        auth_result = auth.authenticate()
        print("Authentication successful:", auth_result)

        # Once authenticated, use the token to initiate payment
        if auth.access_token:  # Ensure the token is set correctly
            payment = CustomerInitiatedPayment(auth)
            payment_data = {
                "CommandID": "CustomerPayBillOnline",
                "Amount": 11,
                "Msisdn": "251700100100",
                "BillRefNumber": "101010",
                "ShortCode": "101010"
            }

            result = payment.customer_initiated_payment(payment_data)
            if result:
                print("Payment successful:", result)
            else:
                print("Payment failed.")
        else:
            print("No token found. Authentication failed.")
    
    except Exception as e:
        print("Error during authentication or payment:", e)


if __name__ == "__main__":
    test_customer_initiated_payment()

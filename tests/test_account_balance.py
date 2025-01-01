from auth.auth import Auth
from account_balance.account_balance import AccountBalance

Auth_URL = "https://apisandbox.safaricom.et/v1/token/generate?grant_type=client_credentials"

def test_account_balance():
    auth  = Auth(base_url=Auth_URL)
    try:
        auth_result = auth.authenticate()
        print("Authentication successful:", auth_result)

        if auth.access_token:
            account_balance = AccountBalance(auth)
            account_balance_data = {
                "Initiator": "testapi",
                "SecurityCredential": "K2tH8KzkmIjCSEOAwgiI6T4ThpQT2DQa/rZfRc8+6iYA62vIsCUhhV0yxM84p0O/70aAiJ6EZwr/bE17Ww1VPMpzPwBadgf+dTwdz8LueZi4kUyZleoIYiJ3jNjkaXMT2g29JHJKRePbd4fsk+y38avf9zl5HG1N9UrpjaT2LhZOjmmPj4U1P/l3NP9C+AlcbAtHmtrkyIhvPrH4XwtDZasRcxUpPMbVcvajaBrcixIga8I4bvfBJfsnspSmpSDoTZ1f9glMYy1qRD83NX6R4/ToD0K0n7z0tKo35rJIn6a1bpVqKXuPmrkcK9ck0nAtmPQy8om6pwCmzDu+sG6slg==",
                "CommandID": "AccountBalance",
                "PartyA": "101010",
                "IdentifierType": "4",
                "Remarks": "remark",
                "ResultURL": "https://mydomain.com/api/account-balance/result",
                "QueueTimeOutURL": "https://mydomain.com/account-balance/timeout"
            }
            result = account_balance.account_balance(account_balance_data)
            if result:
                print("Account balance successful:", result)
            else:
                print("Account balance failed.")
    except Exception as e:
        print("Error during authentication or account balance:", e)

if __name__ == "__main__":
    test_account_balance()
    

            

import os
from dotenv import load_dotenv
import requests
import aiohttp
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, ValidationError, field_validator, Field

# Load environment variables from the .env file
load_dotenv()
basic_acess_token = os.getenv("MPESA_ACCESS_TOKEN")
# Define a Pydantic model for validation
class ReferenceDataItem(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

class StkPushRequest(BaseModel):
    MerchantRequestID: str
    BusinessShortCode: str
    Password: str
    Timestamp: str
    TransactionType: str
    Amount: str
    PartyA: str
    PartyB: str
    PhoneNumber: str
    TransactionDesc: str
    CallBackURL: str
    AccountReference: str
    ReferenceData: list[ReferenceDataItem]

    @field_validator('Amount')
    def validate_amount(cls, value):
        try:
            value = float(value)
            if value <= 0:
                raise ValueError('Amount must be greater than zero.')
            return str(value)
        except ValueError:
            raise ValueError('Amount must be a valid number.')
        
# Pydantic model for response validation
class StkPushResponse(BaseModel):
    MerchantRequestID: str
    CheckoutRequestID: str
    ResponseCode: str
    ResponseDescription: str
    CustomerMessage: str


class PaymentPayloadForPushCheckout(BaseModel):
    MerchantRequestID: Optional[str]
    BusinessShortCode: Optional[str]
    Password: Optional[str]
    Timestamp: Optional[str]
    TransactionType: Optional[str]
    Amount: Optional[str]
    PartyA: Optional[str]
    PartyB: Optional[str]
    PhoneNumber: Optional[str]
    TransactionDesc: Optional[str]
    CallBackURL: Optional[str]
    AccountReference: Optional[str]
    ReferenceData: Optional[List[ReferenceDataItem]]

    class Config:
        # Allow extra fields that might not be in the model
        extra = "allow"

class PaymentPayloadForRegisterURL(BaseModel):
    ShortCode: Optional[str]
    ResponseType: Optional[str]
    CommandID: Optional[str]
    ConfirmationURL: Optional[str]
    ValidationURL: Optional[str]
    class Config:
        # Allow extra fields that might not be in the model
        extra = "allow"

# Responses validation for Register URL
class ResponseHeader(BaseModel):
    responseCode: int = Field(..., description="The HTTP response code.")
    responseMessage: str = Field(..., description="Message describing the response.")
    customerMessage: str = Field(..., description="Message intended for the customer.")
    timestamp: str = Field(..., description="Timestamp of when the response was generated.")

class ApiResponse(BaseModel):
    header: ResponseHeader = Field(..., description="Details of the response header.")

# Payout validation using pydantic
class PaymentPayloadForPayOut(BaseModel):
    InitiatorName: Optional[str]
    SecurityCredential: Optional[str]
    Occassion: Optional[str]
    CommandID: Optional[str]
    PartyA: Optional[str]
    PartyB: Optional[str]
    Remarks: Optional[str]
    Amount: Optional[int]
    QueueTimeOutURL: Optional[str]
    ResultURL: Optional[str]
    class Config:
        # Allow extra fields that might not be in the model
        extra = "allow"

# Pydantic model for response validation for pay out
class PayoutResponse(BaseModel):
    ConversationID: str = Field(..., description="Conversation ID...") 
    OriginatorConversationID: str = Field(..., description="Originator conversation ID...")
    ResponseCode: str = Field(..., description="Response code...")
    ResponseDescription: str = Field(..., description="Response description...")
    
class Mpesa:
    # make auth optional in below method
    def __init__(self, auth=None):
        self.auth = auth

    def stk_push(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Sends an STK Push request to Safaricom API."""

        url = "https://apisandbox.safaricom.et/mpesa/stkpush/v3/processrequest"
        headers = {
            "Authorization": f"Bearer {self.auth.access_token}",
            "Content-Type": "application/json"
        }

        try:
            # Validate the request body using Pydantic
            validated_payload = StkPushRequest(**payload)

            # Sending the POST request synchronously using requests
            response = requests.post(url, json=validated_payload.dict(), headers=headers, timeout=10)

            # Raise exception for 4xx/5xx errors
            response.raise_for_status()

            # Parse and validate the response
            response_data = response.json()

            validated_response = StkPushResponse(**response_data)

            return validated_response.dict()

        except requests.Timeout:
            raise Exception("Request timed out. Please try again later.")
        except requests.RequestException as e:
            raise Exception(f"Network error occurred: {str(e)}")
        except ValidationError as e:
            raise ValueError(f"Invalid data: {e}")
   
    def register_url(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Register the URL with the provided payload.

        :return: Response data or error message.
        """
        endpoint = "https://apisandbox.safaricom.et/v1/c2b-register-url/register"
        url = f"{endpoint}?apikey={basic_acess_token}"

        try: 
            validated_payload = PaymentPayloadForRegisterURL(**payload)

            response = requests.post(url, json= validated_payload.dict())

            response.raise_for_status()

            response_data = response.json()

            validated_response = ApiResponse(**response_data)

            return validated_response.dict()
        
        except requests.Timeout:
            raise Exception("Request timed out. Please try again later.")
        except requests.RequestException as e:
            raise Exception(f"Network error occurred: {str(e)}")
        except ValidationError as e:
            raise ValueError(f"Invalid data: {e}")
        


            
    # async function for pay out
    async def pay_out(self, payload: Any):
            """ Initiate a payout """
                        
            url = "https://apisandbox.safaricom.et/mpesa/b2c/v2/paymentrequest"

            headers = {
                "Authorization": f"Bearer {self.auth.access_token}",
                "Content-Type": "application/json"
            }

            try:
                validated_payload = PaymentPayloadForPayOut(**payload)

                response = requests.post(url, json=validated_payload.dict(), headers=headers, timeout=10)

                response.raise_for_status()

                response_data = response.json()

                validated_payload  = PayoutResponse(**response_data)

                return validated_payload.dict()
            except requests.Timeout:
                raise Exception("Request timed out. Please try again later.")
            except requests.RequestException as e:
                raise Exception(f"Network error occurred: {str(e)}")
            except ValidationError as e:
                raise Exception(f"Invalid payload: {e}")
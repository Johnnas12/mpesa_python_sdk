import os
import requests
from typing import Any, Dict
from dotenv import load_dotenv
from pydantic import BaseModel, Field, field_validator

# Load environment variables from the .env file
load_dotenv()

# Retrieve access token from environment variable
basic_access_token = os.getenv("MPESA_ACCESS_TOKEN")

# Pydantic model to validate the response structure
class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "Bearer"  # Default to "Bearer" if not provided
    expires_in: int = 3599  # Default to 3599 if not provided

    # Custom validation for access_token, ensuring it's a non-empty string
    @field_validator('access_token')
    def check_access_token(cls, value):
        if not value:
            raise ValueError('Access token cannot be empty.')
        return value

# Pydantic model to validate the request headers
class AuthRequestHeaders(BaseModel):
    Authorization: str

class Auth:
    def __init__(self):
        self.access_token = None

    def authenticate(self) -> Dict[str, Any]:
        """Synchronously authenticate and retrieve the access token."""
        
        # Return the token if already authenticated
        if self.access_token:
            print("Token already available.")
            return {"access_token": self.access_token, "token_type": "Bearer", "expires_in": 3599}

        url = "https://apisandbox.safaricom.et/v1/token/generate?grant_type=client_credentials"  # Hardcoded URL
        
        headers = {
            "Authorization": f"Basic {basic_access_token}"  # Use the basic access token
        }

        # Validate the headers with Pydantic model
        try:
            validated_headers = AuthRequestHeaders(**headers)  # Validate headers
        except Exception as e:
            raise ValueError(f"Invalid headers: {e}")

        try:
            # Use requests for synchronous HTTP requests
            response = requests.get(url, headers=headers, timeout=10)

            # Raise exception for 4xx/5xx errors
            response.raise_for_status()

            # If successful, parse and return the response
            data = response.json()

            # Validate the response with Pydantic model
            try:
                validated_response = AuthResponse(**data)  # Validate response
            except Exception as e:
                raise ValueError(f"Invalid response data: {e}")

            # Save the token for further use
            self.access_token = validated_response.access_token

            # Return the validated response
            return validated_response.model_dump()

        except requests.Timeout:
            raise Exception("Request timed out. Please try again later.")
        except requests.RequestException as e:
            raise Exception(f"Network error occurred: {str(e)}")
        except KeyError:
            raise Exception("Authentication response did not contain 'access_token'.")


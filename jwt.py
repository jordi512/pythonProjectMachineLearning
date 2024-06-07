import json
from base64 import urlsafe_b64encode, urlsafe_b64decode
import hashlib
import hmac

SECRET_KEY = "VERVERY_HARD_KEY256"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_header(alg="HS256"):
    """Creates the JWT header as a base64 encoded string."""
    header = {"alg": alg, "typ": "JWT"}
    return urlsafe_b64encode(json.dumps(header).encode()).decode()


def create_payload(data: dict, exp=None):
    """Creates the JWT payload as a base64 encoded string."""
    if exp:
        data["exp"] = exp.timestamp()
    return urlsafe_b64encode(json.dumps(data).encode()).decode()


def create_access_token(data: dict):
    """Encodes a JWT using the provided secret key and payload."""
    global HEADERS, ENCODED_PAYLOAD, SIGNATURE  # Declare global variables
    header = create_header(ALGORITHM)
    encoded_payload = create_payload(data)
    signing_string = f"{header}.{encoded_payload}".encode()
    signature = hmac.new(SECRET_KEY.encode(), signing_string, digestmod=hashlib.sha256).digest()
    encoded_signature = urlsafe_b64encode(signature).decode()
    HEADERS = header
    ENCODED_PAYLOAD = encoded_payload
    SIGNATURE = encoded_signature
    return (header, encoded_payload, encoded_signature)


def verify_signature():
    """Verifies the JWT signature using the provided secret key."""
    signing_string = f"{HEADERS}.{ENCODED_PAYLOAD}".encode()
    expected_signature = hmac.new(SECRET_KEY.encode(), signing_string, digestmod=hashlib.sha256).digest()

    try:
        decoded_signature = urlsafe_b64decode(SIGNATURE)
    except (TypeError, ValueError) as e:
        print(f"Error decoding signature: {e}")
        return False

    return hmac.compare_digest(expected_signature, decoded_signature)


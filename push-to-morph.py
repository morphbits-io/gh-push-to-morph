import argparse
import os
from pprint import pprint

import openapi_client
import base64
import json
import logging
from neo3.wallet.account import Account
from neo3.core import cryptography
from openapi_client import SignedSessionToken, GetUserResponse, DefaultApi, SessionToken

# Constants
MORPH_USER_PASSWORD_ENV_NAME = "MORPH_USER_PASSWORD"
PORT_9100 = 9100
API_VERSION = "api/v0.8"

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def parse_args() -> argparse.Namespace:
    """
    Parses command line arguments.

    Returns:
        Namespace: The parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Publish Allure report to Morph object storage")
    parser.add_argument("--username", required=True, type=str, help="Username for Morph object storage account")
    parser.add_argument("--url", required=True, type=str,
                        help="Morph object storage address. Example: http://localhost, http://example.com")
    parser.add_argument("--port", required=False, type=int, help="Morph object storage port", default=PORT_9100)
    parser.add_argument("--bucket", required=True, type=str, help="Bucket name for your Allure report data")
    parser.add_argument("--report", required=True, type=str,
                        help="Path to the Allure report file")
    return parser.parse_args()


def get_password() -> str:
    """
    Retrieves Morph user password from environment variables.

    Returns:
        str: The password.
    """
    logging.debug(f"Morph password retrieved from environment variable: {MORPH_USER_PASSWORD_ENV_NAME}")
    return os.getenv(MORPH_USER_PASSWORD_ENV_NAME)


def get_host(url: str, port: int) -> str:
    """
    Constructs the full host URL for the Morph API.

    Args:
        url (str): The base URL.
        port (int): The port number.

    Returns:
        str: The full host URL.
    """
    host = f"{url}:{port}/{API_VERSION}"
    logging.debug(f"Constructed Morph full host URL: {host}")
    return host


def get_user_api_response(api_instance: DefaultApi, file_name: str) -> GetUserResponse:
    """
    Fetches user information from the Morph API.

    Args:
        api_instance (DefaultApi): The API client instance.
        file_name (str): The file name.

    Returns:
        GetUserResponse: The user's API response.
    """
    try:
        response = api_instance.get_user(file_name)
        logging.debug(f"API response for user: {response}")
        logging.info("Fetched user information successfully.")
        return response
    except Exception as e:
        logging.error(f"Error fetching user information: {e}")
        raise


def get_private_key(api_instance: DefaultApi, file_name: str) -> str:
    """
    Processes the user's API response to extract the private key.

    Args:
        api_instance (DefaultApi): The API client instance.
        file_name (str): The file name.

    Returns:
        str: The user's private key.
    """
    response = get_user_api_response(api_instance, file_name)
    decoded_bytes = base64.b64decode(response.key)
    decoded_string = decoded_bytes.decode('utf-8')
    json_data = json.loads(decoded_string)
    private_key = json_data['accounts'][0]['key']
    logging.debug(f"Private key extracted from API response: {private_key}")
    logging.info("Processed API response to extract private key successfully.")
    return private_key


def get_public_key(private_key: str, password: str) -> str:
    """
    Get public key from public key

    Args:
        private_key (str): The user's private key.
        password (str): The Morph password.

    Returns:
        str: The user's public key.
    """
    public_key_hex = str(
        cryptography.KeyPair(Account.private_key_from_nep2(private_key, password)).public_key)
    public_key_64 = bytes.fromhex(public_key_hex)
    public_key = base64.b64encode(public_key_64).decode()
    logging.debug(f"Public key: {public_key}")
    logging.info("Get public key from private key successfully.")
    return public_key


def sign_session_tokens(four_session_tokens: list[SessionToken], private_key: str, morph_password: str) -> list[SignedSessionToken]:
    """
    Signs each session token.

    Args:
        four_session_tokens (list[SessionToken]): A list of session tokens.
        private_key (str): The user's private key.
        morph_password (str): The Morph password.

    Returns:
        list[SignedSessionToken]: A list of signed session tokens.
    """
    signed_session_tokens = []
    for token in four_session_tokens:
        public_key_sign_b = cryptography.sign(base64.b64decode(token.session),
                                              Account.private_key_from_nep2(private_key, morph_password))
        encoded_sig = base64.b64encode(public_key_sign_b).decode('utf-8')
        session_token_obj = SignedSessionToken(
            payload=token.payload,
            verb=token.verb,
            signature=encoded_sig
        )
        signed_session_tokens.append(session_token_obj)
    logging.info("Session tokens signed successfully.")
    logging.debug(f"Signed session tokens: {signed_session_tokens}")
    return signed_session_tokens


def get_unified_token(api_instance: DefaultApi, bucket: str, public_key: str, private_key: str, morph_password: str) -> str:
    """
        Get unified morph token.

        Args:
            api_instance (DefaultApi): The API client instance.
            bucket(str): Bucket name.
            public_key(str): The user's public key.
            private_key (str): The user's private key.
            morph_password (str): The Morph password.


        Returns:
            str: Unified session token.
        """
    try:
        api_response = api_instance.create_session(bucket, public_key)
        four_session_tokens = api_response
        signed_session_tokens = sign_session_tokens(four_session_tokens, private_key, morph_password)
        logging.info("Created session and obtained session tokens.")
    except Exception as e:
        logging.error(f"Error during session creation: {e}")
        raise

    try:
        api_response = api_instance.store_session(x_morph_public_key=public_key,
                                                  signed_session_token=signed_session_tokens)
        unified_token = api_response.token
        logging.info("Session tokens stored successfully.")
    except Exception as e:
        logging.error(f"Error storing session tokens: {e}")
        raise

    logging.debug(f"Unified session token: {public_key}")
    logging.info("Get unified session token. successfully.")
    return unified_token



def main():
    args = parse_args()
    logging.info("Starting push Allure report to Morph object storage...")
    morph_password = get_password()
    morph_host = get_host(args.url, args.port)
    data = args.report
    bucket = args.bucket
    username = args.username
    object_name = os.path.basename(data)
    logging.debug(f"username: {username}, host: {morph_host}, bucket: {bucket}, report: {data}")

    configuration = openapi_client.Configuration(host=morph_host)

    with openapi_client.ApiClient(configuration) as api_client:
        api_instance = openapi_client.DefaultApi(api_client)
        private_key = get_private_key(api_instance, username)
        public_key = get_public_key(private_key, morph_password)
        unified_token = get_unified_token(api_instance, bucket, public_key, private_key, morph_password)

        try:
            api_instance.create_object(bucket, public_key, unified_token, object_name, data)
            logging.info("Object created successfully.")
        except Exception as e:
            logging.error(f"Error creating object in Morph storage: {e}")
            raise


if __name__ == "__main__":
    main()

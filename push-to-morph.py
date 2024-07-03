import argparse
import os

import openapi_client
import logging
from openapi_client.models.v1_login_request import V1LoginRequest
# Constants
MORPH_USER_PASSWORD_ENV_NAME = "MORPH_USER_PASSWORD"
PORT_443 = 443
DEFAULT_LIFETIME = 0

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
    parser.add_argument("--port", required=False, type=int, help="Morph object storage port", default=PORT_443)
    parser.add_argument("--bucket", required=True, type=str, help="Bucket name for your Allure report data")
    parser.add_argument("--report", required=True, type=str,
                        help="Path to the Allure report file")
    parser.add_argument("--lifetime", required=False, type=int, help="Morph object storage port", default=DEFAULT_LIFETIME)
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
    host = f"{url}:{port}/api"
    logging.debug(f"Constructed Morph full host URL: {host}")
    return host


def main():
    args = parse_args()
    logging.info("Starting push Allure report to Morph object storage...")
    morph_password = get_password()
    morph_host = get_host(args.url, args.port)
    data = args.report
    bucket = args.bucket
    username = args.username
    object_name = os.path.basename(data)
    lifetime = args.lifetime
    logging.debug(f"username: {username}, host: {morph_host}, bucket: {bucket}, report: {data}, lifetime: {lifetime}")

    configuration = openapi_client.Configuration(host=morph_host)

    with openapi_client.ApiClient(configuration) as api_client:
        api_instance = openapi_client.DefaultApi(api_client)
        login_response = api_instance.v1_login(
            V1LoginRequest.from_dict({"login": username, "password": morph_password})
        ).to_dict()

        try:
            api_instance.v1_create_object(bucket, login_response["token"], object_name, data, lifetime)
            logging.info("Object created successfully.")
        except Exception as e:
            logging.error(f"Error creating object in Morph storage: {e}")
            raise


if __name__ == "__main__":
    main()

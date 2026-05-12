import argparse
import base64
import logging
import os

import openapi_client

# Constants
MORPH_TOKEN_ENV_NAME = "MORPH_TOKEN"
PORT_443 = 443
DEFAULT_LIFETIME = 0

# Configure logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def parse_args() -> argparse.Namespace:
    """
    Parses command line arguments.

    Returns:
        Namespace: The parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Publish Allure report to Morph object storage"
    )
    parser.add_argument(
        "--url",
        required=True,
        type=str,
        help="Morph object storage address. Example: http://localhost, http://example.com",
    )
    parser.add_argument(
        "--port",
        required=False,
        type=int,
        help="Morph object storage port",
        default=PORT_443,
    )
    parser.add_argument(
        "--bucket",
        required=True,
        type=str,
        help="Bucket name for your Allure report data",
    )
    parser.add_argument(
        "--report", required=True, type=str, help="Path to the Allure report file"
    )
    parser.add_argument(
        "--lifetime",
        required=False,
        type=int,
        help="Morph object storage port",
        default=DEFAULT_LIFETIME,
    )
    return parser.parse_args()


def get_token() -> str:
    """
    Retrieves the Morph Bearer token from the environment.

    Returns:
        str: The Bearer token.
    """
    token = os.getenv(MORPH_TOKEN_ENV_NAME)
    if not token:
        raise RuntimeError(
            f"{MORPH_TOKEN_ENV_NAME} environment variable is not set. "
            "Run create-bucket-and-token.py to issue one."
        )
    logging.debug(
        f"Morph token retrieved from environment variable: {MORPH_TOKEN_ENV_NAME}"
    )
    return token


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
    morph_token = get_token()
    morph_host = get_host(args.url, args.port)
    report_path = args.report
    bucket = args.bucket
    object_name = os.path.basename(report_path)
    lifetime = args.lifetime
    logging.debug(
        f"host: {morph_host}, bucket: {bucket}, report: {report_path}, lifetime: {lifetime}"
    )

    # The API expects the object name as a base64-encoded X-Morph-Path header
    # and the request body as the raw object bytes.
    encoded_object_name = base64.b64encode(object_name.encode("utf-8")).decode("ascii")
    with open(report_path, "rb") as fh:
        body = fh.read()

    configuration = openapi_client.Configuration(host=morph_host)

    with openapi_client.ApiClient(configuration) as api_client:
        api_instance = openapi_client.DefaultApi(api_client)

        try:
            api_instance.v1_create_object(
                bucket,
                x_morph_path=encoded_object_name,
                x_morph_lifetime=lifetime,
                body=body,
                _headers={"Authorization": f"Bearer {morph_token}"},
            )
            logging.info("Object created successfully.")
        except Exception as e:
            logging.error(f"Error creating object in Morph storage: {e}")
            raise


if __name__ == "__main__":
    main()

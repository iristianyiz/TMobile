"""
Hooks for the T-Mobile Quality on Demand SDK
"""

# pylint: disable=line-too-long,too-few-public-methods,too-many-arguments,global-statement

import hashlib
import base64
import json
import time
from typing import Any
import uuid
import urllib.parse
from datetime import datetime, timedelta, timezone

import jwt
import requests


class AuthenticationError(Exception):
    """
    Custom error class for auth errors
    """

    def __init__(self, message):
        super().__init__(message)


class Request:
    """
    Hooks request object
    """

    def __init__(self, method, url, headers, body=""):
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body

    def __str__(self):
        return f"Request(method={self.method}, url={self.url}, headers={self.headers}, body={self.body})"


class Response:
    """
    Hooks response object
    """

    def __init__(self, status, headers, body):
        self.status = status
        self.headers = headers
        self.body = body

    def __str__(self):
        return (
            f"Response(status={self.status}, headers={self.headers}, body={self.body})"
        )


# Define module-level variables for CURRENT_TOKEN and CURRENT_EXPIRY
CURRENT_TOKEN = ""
CURRENT_EXPIRY = -1


class CustomHook:
    """
    Custom hook for the T-Mobile Quality on Demand SDK
    """

    def _create_jwt_pop_token_from_request(
        self, request: Request, private_key: str
    ) -> None:
        self._create_jwt_pop_token(
            request.url, request.method, request.headers, request.body, private_key
        )

    def _create_jwt_pop_token(
        self, url: str, method: str, headers: dict, body: Any, private_key: str
    ) -> None:
        """
        Creates a JWT PopToken

        :param request: The request object
        :type request: Request
        :param private_key: The private key to sign the JWT with
        :type private_key: str
        :return: The signed JWT
        :rtype: str
        """

        try:
            # Define arrays for the headers and the fields
            edts = []
            ehts = []

            # Add the headers to the headers and EHTS
            for header in headers:
                edts.append(headers[header])
                ehts.append(header)

            # Add the URI to the headers and EHTS
            # For the URI, we only need the path, not the full URL
            parsed_url = urllib.parse.urlparse(url)
            edts.append(parsed_url.path)
            ehts.append("uri")

            # Add the HTTP method to the headers and EHTS
            edts.append(method)
            ehts.append("http-method")

            # If there is a body, add it to the headers
            # Always add body to the EHTS
            ehts.append("body")
            if body:
                edts.append(json.dumps(body))

            # Create the JWT body
            jwt_body = {}
            jwt_body["edts"] = (
                base64.urlsafe_b64encode(
                    hashlib.sha256(str("".join(edts)).encode("utf-8")).digest()
                )
                .decode("utf-8")
                .rstrip("=")
            )
            jwt_body["v"] = "1"
            jwt_body["exp"] = int(
                (datetime.now(timezone.utc) + timedelta(minutes=2)).timestamp()
            )
            jwt_body["ehts"] = ";".join(ehts)
            jwt_body["iat"] = int(datetime.now(timezone.utc).timestamp())
            jwt_body["jti"] = str(uuid.uuid4())

            # Sign the JWT
            pop_token = jwt.encode(jwt_body, private_key, algorithm="RS256")
            headers["X-Authorization"] = pop_token
        except Exception as error:
            raise AuthenticationError(
                "Error signing the request. Please check your credentials."
            ) from error

    def __get_access_token(
        self, request: Request, client_id: str, client_secret: str, private_key: str
    ) -> None:
        """
        Get the access token using oAuth and set it on the request header as a bearer token.
        """
        # Declare these as global to modify the module-level variables
        global CURRENT_TOKEN, CURRENT_EXPIRY

        # Check if CURRENT_TOKEN is missing or CURRENT_EXPIRY is in the past
        # For the expiry, we add a 10 second buffer to ensure the token is still valid when we use it
        # If so, get a fresh OAuth token
        if not CURRENT_TOKEN or CURRENT_EXPIRY < (time.time() - 10):
            # print("Current token is either missing or has expired")

            # Build the endpoint to get the OAuth token
            parsed_url = urllib.parse.urlparse(request.url)
            oauth_url = f"{parsed_url.scheme}://{parsed_url.netloc}/oauth2/v2/tokens"

            # Fetch a fresh OAuth token
            # Retrieve the new access token and expiry, and set them to the global variables
            token_response = self.__do_token_post(
                oauth_url, client_id, client_secret, private_key
            )

            if not token_response:
                raise AuthenticationError("Error in getting the OAuth token")

            expires_in = token_response["expires_in"]
            access_token = token_response["access_token"]

            if not expires_in or not access_token:
                raise AuthenticationError("Error in getting the OAuth token")

            CURRENT_EXPIRY = int(time.time()) + int(expires_in) * 1000
            CURRENT_TOKEN = access_token

            # print("New token has been set: ", CURRENT_TOKEN)
            # print("New expiry has been set: ", CURRENT_EXPIRY)
        # else:
        #     print("Current token has not expired: ")

        # Set the Bearer token in the request header
        authorization = f"Bearer {CURRENT_TOKEN}"
        request.headers["Authorization"] = authorization

    def __do_token_post(
        self, url_endpoint, client_id, client_secret, private_key: str
    ) -> dict:
        """
        Make a POST request to the oAuth server to get the access token
        """

        token = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode(
            "ascii"
        )

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {token}",
        }

        # Add the PoPToken to the headers
        self._create_jwt_pop_token(url_endpoint, "POST", headers, None, private_key)

        try:
            response = requests.post(url_endpoint, headers=headers, timeout=10)
            response.raise_for_status()

            response_data = response.json()

            if "expires_in" in response_data and "access_token" in response_data:
                return response_data

            # print("Response is missing 'expires_in' or 'access_token'")
            raise AuthenticationError("Error in getting the OAuth token")

        except Exception as error:
            # print("Error in posting the request:", error)
            raise AuthenticationError("Error in getting the OAuth token") from error

    def before_request(self, request: Request, **kwargs):
        """
        Before request hook - adds the PoPToken to the request headers,
        and adds the Bearer string to the Authorization header if it is not present.

        PopToken
        --------

        The PoPToken is set in the X-Authorization header. This needs to be generated
        and added to the request before it is sent.

        Access Token
        ------------

        If you don't have an access token, the client ID and client secret passed
        in the **kwargs will be used to generate one.

        This will then be send to the API with each call.

        :param request: The request object
        :type request: Request
        """

        # Validate the client_id and client_secret from the kwargs
        client_id = kwargs.get("client_id")
        client_secret = kwargs.get("client_secret")
        private_key = kwargs.get("private_key")

        # Check if the client_id and client_secret are set, if not, throw an exception
        if not client_id or not client_secret:
            raise AuthenticationError("Missing CLIENT_ID and/or CLIENT_SECRET")

        if not private_key:
            raise AuthenticationError("Missing PRIVATE_KEY")

        # Get the access token from the oAuth server and set it on the request
        self.__get_access_token(request, client_id, client_secret, private_key)

        # PoPToken
        # This has to be done last as we need to include any modifications to the headers

        # Generate the PoPToken
        self._create_jwt_pop_token_from_request(request, private_key)

    def after_response(self, request: Request, response: Response, **kwargs):
        """
        No-op
        """

    # pylint: disable=unused-argument
    def on_error(
        self, error: Exception, request: Request, response: Response, **kwargs: Any
    ) -> None:
        """
        Handle errors by raising an exception with the status and message from the response.

        Args:
            error (Exception): The original exception.
            request (Request): The request object.
            response (Response): The response object.
            **kwargs: Additional keyword arguments.
        """
        if response.body and "message" in response.body and "status" in response.body:
            # pylint: disable=W0719
            raise Exception(f"{response.body['status']} - {response.body['message']}")

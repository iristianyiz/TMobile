from .services.session import SessionService
from .net.environment import Environment


class TmodeQod:
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        private_key: str = None,
        base_url: str = Environment.DEFAULT.value,
        timeout: int = 60000,
    ):
        """
        Initializes TmodeQod the SDK class.
        """
        self.session = SessionService(base_url=base_url)
        self.set_additional_variables(client_id, client_secret, private_key)
        self.set_timeout(timeout)

    def set_base_url(self, base_url):
        """
        Sets the base URL for the entire SDK.
        """
        self.session.set_base_url(base_url)

        return self

    def set_additional_variables(
        self, client_id: str = None, client_secret: str = None, private_key: str = None
    ):
        """
        Sets the additional variables for the entire SDK.
        """
        self.session.set_additional_variables(client_id, client_secret, private_key)

        return self

    def set_timeout(self, timeout: int):
        """
        Sets the timeout for the entire SDK.

        :param int timeout: The timeout (ms) to be set.
        :return: The SDK instance.
        """
        self.session.set_timeout(timeout)

        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c

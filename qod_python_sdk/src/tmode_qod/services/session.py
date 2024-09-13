from typing import Any
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.session_info import SessionInfo
from ..models.create_session import CreateSession


class SessionService(BaseService):

    @cast_models
    def create_session(
        self, request_body: CreateSession, x_correlator: str = None
    ) -> SessionInfo:
        """Create QoS Session to manage latency/throughput priorities

        If the qosStatus in the API response is "AVAILABLE" means the QoS Session created successfully.

        IMPORTANT: Callback Notifiications functionality will be implemented in future releases

        :param request_body: The request body.
        :type request_body: CreateSession
        :param x_correlator: The transaction ID is GUID. Represents the API transaction, for use in debugging., defaults to None
        :type x_correlator: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Session created
        :rtype: SessionInfo
        """

        Validator(CreateSession).validate(request_body)
        Validator(str).is_optional().validate(x_correlator)

        serialized_request = (
            Serializer(f"{self.base_url}/sessions", self.get_default_headers())
            .add_header("x-correlator", x_correlator)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return SessionInfo._unmap(response)

    @cast_models
    def get_session(self, session_id: str, x_correlator: str = None) -> SessionInfo:
        """Retrieves information for a specific QoS session using the session ID. This endpoint allows you to get the current status and details of the session created via the createSession operation. It is useful for monitoring and debugging purposes.

        :param session_id: Session ID that was obtained from the createSession operation
        :type session_id: str
        :param x_correlator: The transaction ID is GUID. Represents the API transaction, for use in debugging., defaults to None
        :type x_correlator: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Contains information about active session
        :rtype: SessionInfo
        """

        Validator(str).validate(session_id)
        Validator(str).is_optional().validate(x_correlator)

        serialized_request = (
            Serializer(
                f"{self.base_url}/sessions/{{sessionId}}", self.get_default_headers()
            )
            .add_header("x-correlator", x_correlator)
            .add_path("sessionId", session_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return SessionInfo._unmap(response)

    @cast_models
    def delete_session(self, session_id: str, x_correlator: str = None) -> Any:
        """Deletes a specific QoS session using the session ID, freeing up any resources associated with the session. This endpoint is useful for terminating sessions that are no longer needed, ensuring efficient resource management.

        :param session_id: Session ID that was obtained from the createSession operation
        :type session_id: str
        :param x_correlator: The transaction ID is GUID. Represents the API transaction, for use in debugging., defaults to None
        :type x_correlator: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(session_id)
        Validator(str).is_optional().validate(x_correlator)

        serialized_request = (
            Serializer(
                f"{self.base_url}/sessions/{{sessionId}}", self.get_default_headers()
            )
            .add_header("x-correlator", x_correlator)
            .add_path("sessionId", session_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return response

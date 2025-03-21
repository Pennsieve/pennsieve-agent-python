"""
pennsieve2.direct.provider

Gets the user's credentials directly from AWS, not via the Pennsieve Agent.
"""

import boto3
import jwt
import requests

from ..session import APISession, APISessionProvider


class PythonAPISessionProvider(APISessionProvider):
    def __init__(self, api_key, api_secret, api_host, http_session: requests.Session = None):
        super().__init__()
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_host = api_host

        self.cognito_config = None
        self.cognito_idp_client = None
        self._http_session = requests.Session() if http_session is None else http_session

    def new_api_session(self):
        if self.cognito_config is None:
            cc_response = self._http_session.get(f"{self.api_host}/authentication/cognito-config")
            self.cognito_config = CognitoConfig(**cc_response.json())
        init_auth_response = self._initiate_auth()

        access_token = init_auth_response.authentication_result.access_token
        id_token = init_auth_response.authentication_result.id_token

        claims = jwt.decode(id_token, options={"verify_signature": False})
        expiration = claims["exp"]
        organization_node_id = claims["custom:organization_node_id"]
        api_session = APISession(
            token=access_token, expiration=expiration, organization_node_id=organization_node_id
        )

        return api_session

    def clear_session(self, options: dict = None):
        """
        Clears the session and optionally resets the user's parameters.
        :param options: an optional dict containing values for 'api_host', 'api_key', and 'api_secret'
        :return:
        """
        super().clear_session(options)
        if options:
            if "api_host" in options:
                self.api_host = options["api_host"]
            if "api_key" in options:
                self.api_key = options["api_key"]
            if "api_secret" in options:
                self.api_secret = options["api_secret"]
            self.cognito_config = None
            self.cognito_idp_client = None

    def close(self):
        super().close()
        self.cognito_config = None
        self.cognito_idp_client = None

    def _initiate_auth(self):
        if self.cognito_idp_client is None:
            self.cognito_idp_client = boto3.client(
                "cognito-idp",
                region_name=self.cognito_config.region,
                aws_access_key_id="",
                aws_secret_access_key="",
            )

        init_auth_response_dict = self.cognito_idp_client.initiate_auth(
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={"USERNAME": self.api_key, "PASSWORD": self.api_secret},
            ClientId=self.cognito_config.token_pool.app_client_id,
        )

        init_auth_response = InitAuthResponse.from_boto3_response(init_auth_response_dict)
        return init_auth_response


class CognitoConfig:
    def __init__(self, region, userPool, tokenPool, identityPool):
        self.region = region
        self.user_pool = PoolConfig(**userPool)
        self.token_pool = PoolConfig(**tokenPool)
        self.identity_pool = PoolConfig(**identityPool)

    def __str__(self):
        return (
            "{{'region': {0}, 'user_pool': {1}, 'token_pool': {2}, 'identity_pool': {3}}}".format(
                self.region, self.user_pool, self.token_pool, self.identity_pool
            )
        )


class PoolConfig:
    def __init__(self, region, id, appClientId):
        self.region = region
        self.id = id
        self.app_client_id = appClientId

    def __str__(self):
        return str(self.__dict__)


class InitAuthResponse:
    def __init__(self, AuthenticationResult, ChallengeParameters):
        self.authentication_result = AuthenticationResultType(**AuthenticationResult)
        self.ChallengeParameters = ChallengeParameters

    @classmethod
    def from_boto3_response(cls, boto3_response):
        # no need for the response metadata at the moment
        boto3_response.pop("ResponseMetadata", None)
        return cls(**boto3_response)


class AuthenticationResultType:
    def __init__(
        self, AccessToken, ExpiresIn, IdToken, NewDeviceMetadata, RefreshToken, TokenType
    ):
        self.access_token = AccessToken
        self.expires_in = ExpiresIn
        self.id_token = IdToken
        self.new_device_metadata = NewDeviceMetadataType(**NewDeviceMetadata)
        self.refresh_token = RefreshToken
        self.token_type = TokenType


class NewDeviceMetadataType:
    def __init__(self, DeviceGroupKey, DeviceKey):
        self.device_group_key = (DeviceGroupKey,)
        self.device_key = DeviceKey

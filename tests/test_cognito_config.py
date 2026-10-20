from pennsieve.direct.provider import CognitoConfig

POOL = {"region": "us-east-1", "id": "pool-id", "appClientId": "client-id"}


def test_cognito_config_without_identity_pool():
    config = CognitoConfig(region="us-east-1", userPool=POOL, tokenPool=POOL)
    assert config.token_pool.app_client_id == "client-id"


def test_cognito_config_ignores_identity_pool_and_unknown_keys():
    response = {
        "region": "us-east-1",
        "userPool": POOL,
        "tokenPool": POOL,
        "identityPool": {"region": "us-east-1", "id": "", "appClientId": ""},
        "somethingNew": {"x": 1},
    }
    config = CognitoConfig(**response)
    assert config.user_pool.id == "pool-id"
    assert not hasattr(config, "identity_pool")

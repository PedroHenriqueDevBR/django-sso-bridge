import json


class AccessTokenResponse:
    def __init__(
        self,
        access_token: str,
        token_type: str,
        expires_in: int,
        refresh_token: str,
    ) -> None:
        self.access_token = access_token
        self.token_type = token_type
        self.expires_in = expires_in
        self.refresh_token = refresh_token

    def from_json(self, dados: str):
        dicionario = json.loads(dados)
        return AccessTokenResponse(
            access_token=dicionario["access_token"],
            token_type=dicionario["token_type"],
            expires_in=dicionario["expires_in"],
            refresh_token=dicionario["refresh_token"],
        )

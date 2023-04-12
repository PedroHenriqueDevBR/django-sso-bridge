import json

class AuthUser:
    def __init__(
        self,
        full_name: str,
        username: str,
        mail: str,
        registration: str,
        document: str,
        enabled: bool,
        user_type: str,
    ) -> None:
        self.username = username
        self.mail = mail
        self.registration = registration
        self.document = document
        self.enabled = enabled
        self.full_name = full_name
        self.user_type = user_type

    def from_json(self, dados: str):
        dicionario = json.loads(dados)
        return AuthUser(
            full_name=dicionario["full_name"],
            username=dicionario["username"],
            mail=dicionario["mail"],
            registration=dicionario["registration"],
            document=dicionario["document"],
            enabled=dicionario["enabled"],
            user_type=dicionario["user_type"],
        )

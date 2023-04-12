import requests
from django.contrib.auth import login
from django.http.request import HttpRequest
from django.contrib.auth.models import User

from .auth_user import AuthUser
from .access_token_response import AccessTokenResponse


class SSOAuth:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        response_type: str,
        sso_url: str,
        callback_redirect_url: str,
    ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.response_type = response_type
        self.sso_url = sso_url
        self.callback_redirect_url = callback_redirect_url

    def auth_url(self) -> str:
        endpoint = "{}/oauth/authorize".format(self.sso_url)
        return "{}?client_id={}&redirect_uri={}&response_type=code".format(
            endpoint,
            self.client_id,
            self.callback_redirect_url,
        )

    def get_payload(self, permission_token: str):
        return {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": permission_token,
            "grant_type": "authorization_code",
            "redirect_uri": self.callback_redirect_url,
        }

    def get_access_token(
        self,
        request: HttpRequest,
        permission_token,
    ) -> bool:
        endpoint = "{}/oauth/token".format(self.sso_url)
        payload = self.get_payload(permission_token)
        response = requests.post(endpoint, data=payload)

        if response.status_code >= 200 and response.status_code < 300:
            instance = AccessTokenResponse()
            access_data = instance.from_json(dados=response.json)
            access_token = access_data.access_token
            user_data = self.get_user_data(token=access_token)
            self.save_session(request, access_data)
            self.auth(request=request, auth_user_data=user_data)
            return True

        return False

    def save_session(self, request, data):
        request.session.clear()
        request.session["access_token"] = data.access_token
        request.session["validade"] = data.expires_in

    def auth(self, request, auth_user_data: AuthUser):
        search_response = User.objects.filter(username=auth_user_data.username)
        if search_response.exists:
            user = search_response.first
            login(request=request, user=user)
        else:
            user = User.objects.create_user(
                username=auth_user_data.username,
                mail=auth_user_data.mail,
            )
            login(user)

    def get_user_data(self, token) -> AuthUser:
        endpoint = "{}/api/v1/me".format(self.sso_url)
        headers = {"Authorization": "Bearer {}".format(token)}
        response = requests.get(endpoint, headers=headers)
        if response.status_code >= 200 and response.status_code < 300:
            user_instance = AuthUser()
            user = user_instance.from_json(dados=response.json)
            return user

    def logout(self) -> str:
        return "{}/logout".format(self.sso_url)

# google_auth_lib/oauth.py

from google_auth_oauthlib.flow import Flow
from google.oauth2 import id_token
from google.auth.transport import requests
from urllib.parse import urlencode


class AIClubGoogleAuth:
    def __init__(self, config: dict):
        """
        Expected config:
        {
            "client_id": "...",
            "client_secret": "...",
            "redirect_uri": "...",
            "scopes": [ ... ],  # Optional
            "allow_insecure_http": True  # Optional
        }
        """
        self.client_id = config["client_id"]
        self.client_secret = config["client_secret"]
        self.redirect_uri = config["redirect_uri"]
        self.scopes = config.get("scopes", [
            "openid",
            "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/userinfo.profile"
        ])

        if config.get("allow_insecure_http"):
            import os
            os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        self.client_config = {
            "web": {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": [self.redirect_uri],
            }
        }

    def get_authorization_url(self):
        flow = Flow.from_client_config(
            self.client_config,
            scopes=self.scopes,
            redirect_uri=self.redirect_uri
        )
        auth_url, state = flow.authorization_url(prompt="consent")
        return auth_url, state

    def get_user_info(self, query_params: dict, state: str):
        flow = Flow.from_client_config(
            self.client_config,
            scopes=self.scopes,
            state=state,
            redirect_uri=self.redirect_uri
        )
        auth_response = f"{self.redirect_uri}?{urlencode(query_params)}"
        flow.fetch_token(authorization_response=auth_response)

        credentials = flow.credentials
        id_info = id_token.verify_oauth2_token(
            credentials.id_token,
            requests.Request(),
            self.client_id
        )
        return id_info
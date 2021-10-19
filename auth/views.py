from typing import Optional

from base.views import Response


class Token(Response):
    access_token: str
    token_type: str


class TokenData(Response):
    username: Optional[str] = None
from pydantic import BaseModel


class SignupPayload(BaseModel):
    username: str
    pubkey: str
    nonce: str
    signature: str
    pow_token: str


class LoginPayload(BaseModel):
    username: str

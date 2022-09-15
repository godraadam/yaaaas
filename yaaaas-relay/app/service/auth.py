from app.schema.auth import LoginPayload, SignupPayload


class AuthService:
    def auth_user(self, login_payload: LoginPayload):
        raise NotImplementedError()

    def validate_signup_payload(self, payload: SignupPayload) -> bool:
        if not self._validate_signature(
            signature=payload.signature, pubkey=payload.pubkey, nonce=payload.nonce
        ):
            return False
        if not self._validate_pow_token(payload=payload):
            return False
        # additional validation here
        return True

    def _validate_signature(self, signature: str, pubkey: str, nonce: str):
        # validate signature against nonce and signing key
        raise NotImplementedError()

    def _validate_pow_token(self, payload: str):
        # validate that SHA3(payload) <= difficulty
        raise NotImplementedError()


auth_service = AuthService()
